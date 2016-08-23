#Kian8.4 Genome Trimming Commands
##Trimmomatic Command:
```bash
java -jar /work/hdzoo/rhlei/Trimmomatic-0.33/trimmomatic-0.33.jar PE \
        -phred33 \
        /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l280a1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l280a2.fastq \
        kian8.4l280a1_TR_paired.fastq kian8.4l280a1_TR_unpaired.fastq \
        kian8.4l280a2_TR_paired.fastq kian8.4l280a2_TR_unpaired.fastq \
        ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 \
        LEADING:3 \
        TRAILING:3 \
        SLIDINGWINDOW:4:30 \
        MINLEN:70;
```
##NxTrim Command Example:
```bash
nxtrim --separate -1 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka1.fastq -O kian8.4mp6ka1 -2 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka2.fastq
```
##Trimmomatic Post NxTrim
These weren't used in the assemblies.
```bash
cat kian8.4mp8ka1_R1.mp.fastq.gz kian8.4mp8ka1_R1.unknown.fastq.gz > kian8.4m8ka1_R1.mp.unknown.fastq.gz;
cat kian8.4mp8ka1_R2.mp.fastq.gz kian8.4mp8ka1_R2.unknown.fastq.gz > kian8.4m8ka1_R2.mp.unknown.fastq.gz;

R1=kian8.4m8ka1_R1.mp.unknown.fastq.gz
R2=kian8.4m8ka1_R2.mp.unknown.fastq.gz
java -jar /work/hdzoo/rhlei/programs/Trimmomatic-0.33/trimmomatic-0.33.jar PE \
        -phred33 \
        $R1 $R2 \
        ${R1}_trimmed.fastq ${R1}_Fsingle.fastq ${R2}_trimmed.fastq ${R1}_Rsingle.fastq \
        ILLUMINACLIP:/work/hdzoo/rhlei/programs/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 \
        LEADING:3 \
        TRAILING:3 \
        SLIDINGWINDOW:4:30 \
        MINLEN:70;
rm ${R1}_Fsingle.fastq ${R1}_Rsingle.fastq;
```
#Kian8.4 Genome Trimming Results
##220 Insert
```
TrimmomaticPE: Started with arguments: -phred33 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l220a1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l220a2.fastq kian8.4l220a1_TR_paired.fastq kian8.4l220a1_TR_unpaired.fastq kian8.4l220a2_TR_paired.fastq kian8.4l220a2_TR_unpaired.fastq ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 1278960204 Both Surviving: 612312354 (47.88%) Forward Only Surviving: 182714331 (14.29%) Reverse Only Surviving: 103785519 (8.11%) Dropped: 380148000 (29.72%)
TrimmomaticPE: Completed successfully
```
##280 Insert
```
TrimmomaticPE: Started with arguments: -phred33 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l280a1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l280a2.fastq kian8.4l280a1_TR_paired.fastq kian8.4l280a1_TR_unpaired.fastq kian8.4l280a2_TR_paired.fastq kian8.4l280a2_TR_unpaired.fastq ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 397393878 Both Surviving: 242204071 (60.95%) Forward Only Surviving: 54246463 (13.65%) Reverse Only Surviving: 35506002 (8.93%) Dropped: 65437342 (16.47%)
TrimmomaticPE: Completed successfully
```
##800 Insert
```
TrimmomaticPE: Started with arguments: -phred33 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l800a1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4l800a2.fastq kian8.4l800a1_TR_paired.fastq kian8.4l800a1_TR_unpaired.fastq kian8.4l800a2_TR_paired.fastq kian8.4l800a2_TR_unpaired.fastq ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 322777831 Both Surviving: 107757443 (33.38%) Forward Only Surviving: 39428337 (12.22%) Reverse Only Surviving: 23088389 (7.15%) Dropped: 152503662 (47.25%)
TrimmomaticPE: Completed successfully
```
##6k MP (no NxTrim)
```
TrimmomaticPE: Started with arguments: -phred33 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka2.fastq kian8.4mp6ka1_TR_leitest_paired.fastq kian8.4mp6ka1_TR_leitest_unpaired.fastq kian8.4mp6ka2_TR_leitest_paired.fastq kian8.4mp6ka2_TR_leitest_unpaired.fastq ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 219631508 Both Surviving: 118133723 (53.79%) Forward Only Surviving: 29180877 (13.29%) Reverse Only Surviving: 20162657 (9.18%) Dropped: 52154251 (23.75%)
TrimmomaticPE: Completed successfully
```
##8k MP (no NxTrim)
```
TrimmomaticPE: Started with arguments: -phred33 /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp8ka1.fastq /work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp8ka2.fastq kian8.4mp8ka1_TR_paired_leitest.fastq kian8.4mp8ka1_TR_unpaired_leitest.fastq kian8.4mp8ka2_TR_paired_leitest.fastq kian8.4mp8ka2_TR_unpaired_leitest.fastq ILLUMINACLIP:/work/hdzoo/rhlei/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 273244682 Both Surviving: 103619089 (37.92%) Forward Only Surviving: 16320160 (5.97%) Reverse Only Surviving: 56200891 (20.57%) Dropped: 97104542 (35.54%)
TrimmomaticPE: Completed successfully
```
##6k MP Nxtrim + Trimmomatic
###NxTrim
```
R1:	/work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka1.fastq
R2:	/work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp6ka2.fastq
Trimming summary:
205509152 / 219631508	( 93.57% )	reads passed chastity/purity filters.
27784 / 205509152	( 0.01% )	reads had TWO copies of adapter (filtered).
1487156 / 205481368	( 0.72% )	read pairs were ignored because template length appeared less than read length
203994212 remaining reads were trimmed

64458004 / 203994212	( 31.60% )	read pairs had MP orientation
54383362 / 203994212	( 26.66% )	read pairs had PE orientation
76836976 / 203994212	( 37.67% )	read pairs had unknown orientation
8315870 / 203994212	( 4.08% )	were single end reads

20811922 / 203994212	( 10.20% )	extra single end reads were generated from overhangs
```
###Trimmomatic
```
TrimmomaticPE: Started with arguments: -phred33 kian8.4mp6ka1_R1.mp.unknown.fastq.gz kian8.4mp6ka1_R2.mp.unknown.fastq.gz kian8.4mp6ka1_R1.mp.unknown.fastq.gz_trimmed.fastq kian8.4mp6ka1_R1.mp.unknown.fastq.gz_Fsingle.fastq kian8.4mp6ka1_R2.mp.unknown.fastq.gz_trimmed.fastq kian8.4mp6ka1_R1.mp.unknown.fastq.gz_Rsingle.fastq ILLUMINACLIP:/work/hdzoo/rhlei/programs/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 141294980 Both Surviving: 31408932 (22.23%) Forward Only Surviving: 24286075 (17.19%) Reverse Only Surviving: 30357938 (21.49%) Dropped: 55242035 (39.10%)
TrimmomaticPE: Completed successfully
```
##8k MP Nxtrim + Trimmomatic
###NxTrim
```
R1:	/work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp8ka1.fastq
R2:	/work/hdzoo/rhlei/kian8.4tdata/kian8.4o/kian8.4mp8ka2.fastq

Trimming summary:
245974730 / 273244682	( 90.02% )	reads passed chastity/purity filters.
627 / 245974730	( 0.00% )	reads had TWO copies of adapter (filtered).
35480 / 245974103	( 0.01% )	read pairs were ignored because template length appeared less than read length
245938623 remaining reads were trimmed

66481722 / 245938623	( 27.03% )	read pairs had MP orientation
43076519 / 245938623	( 17.52% )	read pairs had PE orientation
136024063 / 245938623	( 55.31% )	read pairs had unknown orientation
356319 / 245938623	( 0.14% )	were single end reads

22023325 / 245938623	( 8.95% )	extra single end reads were generated from overhangs
```
###Trimmomatic
```
TrimmomaticPE: Started with arguments: -phred33 kian8.4m8ka1_R1.mp.unknown.fastq.gz kian8.4m8ka1_R2.mp.unknown.fastq.gz kian8.4m8ka1_R1.mp.unknown.fastq.gz_trimmed.fastq kian8.4m8ka1_R1.mp.unknown.fastq.gz_Fsingle.fastq kian8.4m8ka1_R2.mp.unknown.fastq.gz_trimmed.fastq kian8.4m8ka1_R1.mp.unknown.fastq.gz_Rsingle.fastq ILLUMINACLIP:/work/hdzoo/rhlei/programs/Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:30 MINLEN:70
Multiple cores found: Using 16 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 202505785 Both Surviving: 46371161 (22.90%) Forward Only Surviving: 21317814 (10.53%) Reverse Only Surviving: 53715666 (26.53%) Dropped: 81101144 (40.05%)
TrimmomaticPE: Completed successfully
```
