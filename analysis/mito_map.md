#Map simus reads to the mitochondria
```bash
FASTA=NC_021959Psimus.fasta
bwa mem $FASTA KAR3_S1_R1_001_tr_paired.fq KAR3_S1_R2_001_tr_paired.fq | \
samtools view -bS -F 4 - > KAR3_mapped.bam &
bwa mem $FASTA KIAN81_S4_R1_001_tr_paired.fq KIAN81_S4_R2_001_tr_paired.fq | \
samtools view -bS -F 4 - > KIAN81_mapped.bam &
bwa mem $FASTA RANO355_S3_R1_001_tr_paired.fq RANO355_S3_R2_001_tr_paired.fq | \
samtools view -bS -F 4 - > RANO355_mapped.bam &
bwa mem $FASTA TORO824_S2_R1_001_tr_paired.fq TORO824_S2_R2_001_tr_paired.fq | \
samtools view -bS -F 4 - > TORO824_mapped.bam;
```
#Sort the bams:
```bash
for I in *.bam ; do  samtools sort $I $I.sorted.bam; done
```
#Remove duplicates
```bash
for I in *.bam ; do  samtools rmdup $I $I.rmdup.bam; done
```
