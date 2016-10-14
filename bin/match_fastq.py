#!/usr/bin/env python
from multiprocess import Pool
import os
import subprocess as sp

BWA_PATH = 'bwa'
MARK_DUPLICATES_JAR_PATH = "/bin/MarkDuplicates.jar"
NOVOSORT_PATH = 'novosort'
SAMTOOLS_PATH = 'samtools'


def get_nondirectional_name(*fastq_pairs):
    for fastq in fastq_pairs:
        return "".join([c for c in fastq if i not in ""])


def get_sorted_fastq_with_split(path):
    for fi in sorted(os.listdir(path)):
        if fi.endswith(".fq") or fi.endswith('.fastq'):
            yield 1, fi
        elif fi.endswith(".fq.gz") or fi.endswith('.fastq.gz'):
            yield 2, fi


def split_fastq_by_direction(split_point, fastq):
    start_chars = ""
    end_chars = ""
    non_d_name = ""
    breakpoint = False
    for char in reversed(fastq):
        if not breakpoint:
            if char in "12":
                breakpoint = True
                continue
            end_chars += char
        else:
            start_chars += char
        non_d_name += char
    non_directional_name = non_d_name[::-1].rsplit(".", split_point)[0]
    return start_chars, end_chars, non_directional_name


def get_paired_fastq(path):
    fastqs = get_sorted_fastq_with_split(path)
    prev = ""
    prev_start_chars = ""
    prev_end_chars = ""
    for split_point, fastq in sorted(fastqs):

        start_chars, end_chars, non_d_name = split_fastq_by_direction(
            split_point,
            fastq
        )

        if prev_end_chars == end_chars and start_chars == prev_start_chars:
            yield prev, fastq, non_d_nameNOVOSORT_PATH = 'novosort'
        prev = fastq
        prev_start_chars = start_chars
        prev_end_chars = end_chars


def samtools_index_fasta(fasta_path):
    """ indexes a fasta with samtools """
    cmd = [SAMTOOLS_PATH, 'faidx', fasta_path]
    return cmd


def bwa_index_fasta(fasta_path):
    """ builds a bwa index for a fasta """
    cmd = [BWA_PATH, 'index', fasta_path]
    return cmd


def bwa_mem_cmd(fasta_path, fw_fq, rv_fq):
    """ bwa mem command builder """

    short_fw_fq = get_fastq_file_path(fasta_path, fw_fq)
    short_rv_fq = get_fastq_file_path(fasta_path, rv_fq)

    cmd = [BWA_PATH, 'mem', fasta_path, short_fw_fq, short_rv_fq]

    return cmd


def samtools_view_cmd():
    """ runs samtools view command builder"""
    cmd = [SAMTOOLS_PATH, 'view', '-Su']
    return cmd


def novosort_cmd(bamfile_working):
    """ novosort command builder """
    cmd = [NOVOSORT_PATH,
           '-m', '1g',
           '-o', bamfile_working,
           '-t', '.', '-']
    return cmd


def mark_duplicates_cmd(bamfile_working, bamfile_final):
    """ mark duplicates command builder """
    cmd = ['java', '-jar', MARK_DUPLICATES_JAR_PATH,
           'INPUT={}'.format(bamfile_working),
           'OUTPUT={}'.format(bamfile_final),
           'REMOVE_DUPLICATES=true',
           'METRICS_FILE=dup.txt',
           'ASSUME_SORTED=true']
    return cmd


def samtools_index_bam_cmd(bamfile_final):
    """ bamfile index command maker """
    cmd = [SAMTOOLS_PATH, 'index', bamfile_final]
    return cmd


def build_fasta_indices(fasta_path):
    """ builds fasta indices """
    bwa_cmd = bwa_index_fasta(fasta_path)
    sam_cmd = samtools_index_fasta(fasta_path)

    sp.call(bwa_cmd)
    sp.call(sam_cmd)
    return True


def build_working_bam(ref_file, fw_fq, rv_fq, base_name):
    """ builds first step bamfile """
    bamfile_working = base_name + "_working.bam"
    final_bam = "_final.bam"

    bwa_cmd = bwa_mem_cmd(ref_file, fw_fq, rv_fq)
    sam_cmd = samtools_view_cmd()
    nov_cmd = novosort_cmd(bamfile_working)

    p1 = sp.Popen(bwa_cmd, stdout=sp.PIPE)
    p2 = sp.Popen(sam_cmd, stdin=p1.stdout, stdout=sp.PIPE)
    p3 = sp.Popen(nov_cmd, stdin=p2.stdout)

    status = p3.communicate()

    return bamfile_working, final_bam


def build_final_bam(bamfile_working, bamfile_final):
    """ builds finalized bamfile """
    dups_cmd = mark_duplicates_cmd(bamfile_working, bamfile_final)
    index_bam_cmd = samtools_index_bam_cmd(bamfile_final)

    sp.call(dups_cmd)
    sp.call(index_bam_cmd)

    os.remove(bamfile_working)
    return bamfile_final


def multiprocess_bwa(fasta, paired_fastqs, cores = 8):
    p = Pool(cores)
    build_fasta_indices(fasta)
    all_bam_names = p.map(build_working_bam, ([fasta] + list(fqs) for fqs in paired_fastqs))
    final_bams = p.map(build_final_bam, all_bam_names)


def main():
    fasta = ""
    path = "../Desktop/simus_reads"
    fastqs = get_paired_fastq(path)
    multiprocess_bwa(fasta, fastq_pairs)


if __name__ == "__main__":
    main()
