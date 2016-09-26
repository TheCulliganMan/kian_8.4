#Kian 8.4 PSMC
For loops are usually a good idea...
##Index Fasta
```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
bwa index $REF
```
##Process Reads:
All reads were processed using trimmomatic.  The Toro, Rano, and Kian81 reads
had a ~600 insert length. To match this with the Kian8.4 reads we used the 8.4
~800 insert length sequences.  Then ran his raw reads through trimmomatic at the
same settings, and then clipped the forward and reverse reads with head to the
length of the Kar3 forward sample.

###Trimmomatic for each sample

```bash
java -jar Trimmomatic-0.36/trimmomatic-0.36.jar \
	PE -phred33 \
	kian8.4l800a1.fastq \
	kian8.4l800a2.fastq \
	kian8.4l800a1_tr.fastq \
	kian8.4l800a1_tr_unpaired.fastq \
	kian8.4l800a2_tr.fastq \
        kian8.4l800a2_tr_unpaired.fastq \
	ILLUMINACLIP:Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10 \
	LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36;
```
###Head Processing for Kian8.4
```bash
head -n 408104088 kian8.4l800a1_tr.fastq > kian8.4l800a1_tr_clipped.fastq;
head -n 408104088 kian8.4l800a2_tr.fastq > kian8.4l800a2_tr_clipped.fastq;

head -n 408104088 m_mur_SRR1662129_1_tr.fastq > m_mur_SRR1662129_1_tr.fastq.head_trimmed.fq;
head -n 408104088 m_mur_SRR1662129_2_tr.fastq > m_mur_SRR1662129_2_tr.fastq.head_trimmed.fq;

head -n 408104088 p_coq_SRR1657023_1_tr.fastq > p_coq_SRR1657023_1_tr.fastq.head_trimmed.fq;
head -n 408104088 p_coq_SRR1657023_2_tr.fastq > p_coq_SRR1657023_2_tr.fastq.head_trimmed.fq;
```
###For the high coverage correction 30x coverage
```bash
for I in *fq.gz
do
zcat $I | head -n 1224312264 > $I.clipped.fq
done

```
##Make bamfiles
```bash
REF='mmr_ref_Mmur_2.0_chrUn.fa'
bwa mem -t 32 $REF m_mur_SRR1662129_1_tr.fastq.head_trimmed.fq m_mur_SRR1662129_2_tr.fastq.head_trimmed.fq  > mmur_align.bam
REF='379532_ref_Pcoq_1.0_chrUn.fa'
bwa mem -t 32 $REF p_coq_SRR1657023_1_tr.fastq.head_trimmed.fq p_coq_SRR1657023_2_tr.fastq.head_trimmed.fq > pcoq_align.bam

REF='masurca_mito_y_x_removed.final.contigs.fasta'
bwa mem -t 32 $REF KAR3_S1_R1_001_tr_paired.fq KAR3_S1_R2_001_tr_paired.fq > mass_auto_KAR3.bam;
bwa mem -t 32 $REF KIAN81_S4_R1_001_tr_paired.fq KIAN81_S4_R2_001_tr_paired.fq > mass_auto_KIAN81.bam;
bwa mem -t 32 $REF RANO355_S3_R1_001_tr_paired.fq RANO355_S3_R2_001_tr_paired.fq > mass_auto_RANO.bam;
bwa mem -t 32 $REF TORO824_S2_R1_001_tr_paired.fq TORO824_S2_R2_001_tr_paired.fq > mass_auto_toro824.bam;
bwa mem -t 32 $REF kian8.4l800a1_tr_clipped.fastq kian8.4l800a2_tr_clipped.fastq > mass_auto_kian8.4_800.bam
```
##Sort bamfiles
So this actually goes for the next couple steps.  The apt versions of samtools
and bcftools actually conflict with one another right now.  You can't have both
installed at the same time.  You should compile from source right here
[samtools & bcftools](http://samtools.github.io/bcftools/).
```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
samtools sort --reference $REF -O BAM -o mass_auto_kar3_sorted.bam mass_auto_KAR3.bam &
samtools sort --reference $REF -O BAM -o mass_auto_KIAN81.sorted.bam mass_auto_KIAN81.bam &
samtools sort --reference $REF -O BAM -o mass_auto_RANO.sorted.bam mass_auto_RANO.bam &
samtools sort --reference $REF -O BAM -o mass_auto_toro824.sorted.bam mass_auto_toro824.bam  &
samtools sort --reference $REF -O BAM -o mass_auto_kian8.4_800.sorted.bam mass_auto_kian8.4_800.bam

REF='mmr_ref_Mmur_2.0_chrUn.fa'
samtools sort --reference $REF -O BAM -o mmur_align_sorted.bam mmur_align.bam 

REF='379532_ref_Pcoq_1.0_chrUn.fa'
samtools sort --reference $REF -O BAM -o pcoq_align_sorted.bam pcoq_align.bam
```

##Remove Duplicates
```bash
samtools rmdup mass_auto_kar3_sorted.bam mass_auto_kar3_sorted.nodups.bam &
samtools rmdup mass_auto_KIAN81.sorted.bam mass_auto_KIAN81.sorted.nodups.bam &
samtools rmdup mass_auto_RANO.sorted.bam mass_auto_RANO.sorted.nodups.bam &
samtools rmdup mass_auto_toro824.sorted.bam mass_auto_toro824.sorted.nodups.bam &
samtools rmdup mass_auto_kian8.4_800.sorted.bam mass_auto_kian8.4_800.sorted.nodups.bam

REF='mmr_ref_Mmur_2.0_chrUn.fa'
samtools rmdup --reference $REF mmur_align_sorted.bam mmur_align_sorted.nodups.bam 

REF='379532_ref_Pcoq_1.0_chrUn.fa'
samtools rmdup --reference $REF pcoq_align_sorted.bam pcoq_align_sorted.nodups.bam 
```
##Get the average map coverage:
```bash
for I in *.nodups.bam; do
	echo $I >> cov_stats.txt;
	samtools depth $I |
	awk '{sum+=$3; sumsq+=$3*$3} END { print "Average = ",sum/NR; print "Stdev = ",sqrt(sumsq/NR - (sum/NR)*2)}' >> cov_stats.txt;
done &
```
##Create vcf
So I actually need the vcf file to get an snp count...
```bash
samtools mpileup -C50 -uf $REF mass_auto_kar3_sorted.nodups.bam > mass_auto_KAR3.vcf &
samtools mpileup -C50 -uf $REF mass_auto_KIAN81.sorted.nodups.bam > mass_auto_KIAN81.vcf
samtools mpileup -C50 -uf $REF mass_auto_RANO.sorted.nodups.bam > mass_auto_RANO.vcf
samtools mpileup -C50 -uf $REF mass_auto_toro824.sorted.nodups.bam > mass_auto_toro824.vcf
samtools mpileup -C50 -uf $REF mass_auto_kian8.4_800.sorted.nodups.bam > mass_auto_kian8.4_800.vcf
```
##Process vcf for variant count (not for the next step for the psmc scaling)
```
bcftools call -v -V indels -m mass_auto_kian8.4_800.vcf > kian84.800.called.vcf &
bcftools call -v -V indels -m mass_auto_kar3_sorted.nodups.vcf > kar3.called.vcf &
bcftools call -v -V indels -m mass_auto_KIAN81.sorted.nodups.vcf > kian81.called.vcf &
bcftools call -v -V indels -m mass_auto_RANO.sorted.nodups.vcf > rano.called.vcf &
bcftools call -v -V indels -m mass_auto_toro824.sorted.nodups.vcf > toro824.called.vcf;

for I in *called.vcf; do
	echo $I >> variant_counts.txt;
	grep -c -v "^#" $I >> variant_counts.txt;
done;

```
Another fun little change here.  Bcftools view and bcftools call switched some
functionality a little while ago.  Heng Li's blog recommends
`bcftools view -c -`, but that doesn't work with the newer versions of the
software, so I made a switch.
##Extract fq.gz
```bash
REF='masurca_mito_y_x_removed.final.contigs.fasta'
cat mass_auto_KAR3.vcf | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_KAR3.fq.gz
cat mass_auto_KIAN81.vcf | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_KIAN81.fq.gz
cat mass_auto_RANO.vcf | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_RANO.fq.gz
cat mass_auto_toro824.vcf | bcftools call -c | \
	vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_toro824.fq.gz
cat mass_auto_kian8.4_800.vcf | bcftools call -c | \
  vcfutils.pl vcf2fq -d 10 -D 100 | gzip > mass_auto_kian84.fq.gz
```

##Create .psmc file:
Convert the fq.gz to psmcfa files.
```bash
/psmc/utils/fq2psmcfa -q20 mass_auto_KAR3.fq.gz > mass_auto_KAR3.psmcfa &
/psmc/utils/fq2psmcfa -q20 mass_auto_RANO.fq.gz > mass_auto_RANO.psmcfa &
/psmc/utils/fq2psmcfa -q20 mass_auto_toro824.fq.gz > mass_auto_toro824.psmcfa &
/psmc/utils/fq2psmcfa -q20 mass_auto_KIAN81.fq.gz > mass_auto_KIAN81.psmcfa &
/psmc/utils/fq2psmcfa -q20 mass_auto_kian8.4.fq.gz > mass_auto_kian8.4.psmcfa;
```
This is the basic bootstrapping command.  For an overly complex script to run
things in parallel go to the [psmc bootstrapper](../bin/bootstrap_psmc.py).  
This command works by dragging the file into the psmcfa folder and running.  
Change the default values to fit your project.

```bash
psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o mass_auto_KAR3.psmc mass_auto_KAR3.psmcfa;

seq 100 | xargs -i echo psmc -N25 -t15 -r5 -b -p "4+25*2+4+6" \
	    -o round-{}.psmc split.fa | sh
```
Next plot everything.  I used a [template by Heng Li](http://lh3lh3.users.sourceforge.net/download/chimp-fit.gp) for the boostrap replicates in gnuplot.  We can build text files for this by running the an
[automation script located here](../bin/psmc_plotter.py).  This takes master psmc records and bootstrap replicates and outputs text files into a new subdirectory for gnuplot.  It is fairly specialized to our filenames, but can be easily modified.  This files command is as follows:
```bash
python psmc_plotter <path to bootstrap_dir> <path to another bootstrap_dir>
```
After that you have to edit the [gnuplot template file](../templates/simus_plot.gp).  This file will produce the end psmc graph, ready to be rescaled.
