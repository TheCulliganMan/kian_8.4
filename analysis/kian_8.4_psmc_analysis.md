#Kian 8.4 PSMC
For loops are usually a good idea...
##Index Fasta
```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
bwa index $REF
```
##Make bamfiles
```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
bwa mem -t 32 $REF KAR3_S1_R1_001_tr_paired.fq KAR3_S1_R2_001_tr_paired.fq > mass_auto_KAR3.bam;
bwa mem -t 32 $REF KIAN81_S4_R1_001_tr_paired.fq KIAN81_S4_R2_001_tr_paired.fq > mass_auto_KIAN81.bam;
bwa mem -t 32 $REF RANO355_S3_R1_001_tr_paired.fq RANO355_S3_R2_001_tr_paired.fq > mass_auto_RANO.bam;
bwa mem -t 32 $REF TORO824_S2_R1_001_tr_paired.fq TORO824_S2_R2_001_tr_paired.fq > mass_auto_toro824.bam;
bwa mem -t 32 $REF ../kian8.4l280a1.fastq > mass_auto_kian8.4.bam; #280 insert length
```
##Sort bamfiles
So this actually goes for the next couple steps.  The apt versions of samtools
and bcftools actually conflict with one another right now.  You can't have both
installed at the same time.  You should compile from source right here
[samtools & bcftools](http://samtools.github.io/bcftools/).
```bash
samtools sort --reference $REF -O BAM mass_auto_KAR3.bam -o mass_auto_kar3_sorted.bam &
samtools sort --reference $REF -O BAM mass_auto_KIAN81.bam -o BAM mass_auto_KIAN81.sorted.bam &
samtools sort --reference $REF -O BAM mass_auto_RANO.bam -o mass_auto_RANO.sorted.bam &
samtools sort --reference $REF -O BAM mass_auto_toro824.bam -o mass_auto_toro824.sorted.bam &
samtools sort --reference $REF -O BAM mass_auto_kian8.4.bam -o mass_auto_kian8.4.sorted.bam
```

##Remove Duplicates
```bash
samtools mass_auto_kar3_sorted.bam mass_auto_kar3_sorted.nodups.bam &
samtools mass_auto_KIAN81.sorted.bam mass_auto_KIAN81.sorted.nodups.bam &
samtools mass_auto_RANO.sorted.bam mass_auto_RANO.sorted.nodups.bam &
samtools mass_auto_toro824.sorted.bam mass_auto_toro824.sorted.nodups.bam &
samtools mass_auto_kian8.4.sorted.bam mass_auto_kian8.4.sorted.nodups.bam
```

##Extract fq.gz
Another fun little change here.  Bcftools view and bcftools call switched some
functionality a little while ago.  Heng Li's blog recommends
`bcftools view -c -`, but that doesn't work with the newer versions of the
software, so I made a switch.

```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
samtools mpileup -C50 -uf $REF mass_auto_KAR3.bam | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_KAR3.fq.gz
samtools mpileup -C50 -uf $REF mass_auto_KIAN81.bam | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_KIAN81.fq.gz
samtools mpileup -C50 -uf $REF mass_auto_RANO.bam | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_RANO.fq.gz
samtools mpileup -C50 -uf $REF mass_auto_toro824.bam | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_toro824.fq.gz
```

##Create .psmc file:
This is the basic bootstrapping command.  For an overly complex script to run
things in parallel go to the [psmc bootstrapper](../bin/bootstrap_psmc.py)

```bash
utils/fq2psmcfa -q20 mass_auto_KAR3.fq.gz > mass_auto_KAR3.psmcfa;

psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o mass_auto_KAR3.psmc mass_auto_KAR3.psmcfa;

seq 100 | xargs -i echo psmc -N25 -t15 -r5 -b -p "4+25*2+4+6" \
	    -o round-{}.psmc split.fa | sh

cat mass_auto_KAR3.psmc round-*.psmc > combined.psmc
	utils/psmc_plot.pl -pY50000 combined combined.psmc

```
