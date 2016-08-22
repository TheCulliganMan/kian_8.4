#Kian8.4 Autosome Extraction
##Download programs:
```bash
git clone https://github.com/TheCulliganMan/extract_autosome.git
```
##Run Programs:
```python
import extract_autosome

extract_autosome.extract_autosome(
    "masurca_contigs_parsed.fasta.masked",
    "fasta_splits",
    "fasta_splits",
    "../blast_x_vs_mick/x",
    'hits',
    "x_removed.masurca_contigs_parsed.masked.fasta",
    cores=32
)


extract_autosome.extract_autosome(
    "x_removed.masurca_contigs_parsed.masked.fasta",
    "fasta_splits",
    "fasta_splits",
    "../blast_x_vs_mick/y",
    'hits',
    "y_x_removed.masurca_contigs_parsed.masked.fasta",
    cores=32
)

extract_autosome.extract_autosome(
    "y_x_removed.masurca_contigs_parsed.masked.fasta",
    "fasta_splits",
    "fasta_splits",
    "../blast_x_vs_mick/NC_021959Psimus.fasta",
    'hits',
    "mito_y_x_removed.masurca_contigs_parsed.masked.fasta",
    cores=32
)

extract_autosome.unmask_autosome(
    "mito_y_x_removed.masurca_contigs_parsed.masked.fasta",
    "masurca_contigs_parsed.fasta",
    "mito_y_x_removed.final.contigs.fasta"
)
```

##Length Counter Code:

```python
#!/usr/bin/env python

import sys
from Bio import SeqIO
if len(sys.argv) <= 1:
        exit()
filename = sys.argv[1]

total_len = 0

with open(filename) as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
                total_len += len(record.seq)

print (total_len)
```

##Contig Counter Code

```python
#!/usr/bin/env python
from __future__ import print_function
import sys
from Bio import SeqIO
if len(sys.argv) <= 1:
        exit()
filename = sys.argv[1]

total_contigs = 0

with open(filename) as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
                total_contigs += 1

print("TOTAL CONTIGS", total_contigs)
```

##RESULTS:

###Base Pair Counts:

```
Orignal Sequence Length: 2,238,717,771 bp
After X Removal:         2,011,555,924 bp
After XY Removal:        2,003,065,157 bp
After MitoXY Removal:    2,002,851,803 bp
Difference:                235,865,968 bp
Removed %:                     10.5358 %
```

### Contig Counts:

```
Orignal Contig Count:          211,576
After X Removal:               202,422
After XY Removal:              202,121
After MitoXY Removal:          202,106
Difference:                      9,470
Removed %:                      1.1674 %
```
