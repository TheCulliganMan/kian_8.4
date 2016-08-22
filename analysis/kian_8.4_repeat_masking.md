#Kian8.4 Repeat Masking

##Parse MaSuRCA fasta ids
The fasta ids for the masurca contigs are too long for repeat masker. I had to trim them.

```python
#!/usr/bin/env python

import sys
from Bio import SeqIO

def shorten_fasta_ids(inpu, outpu):
	with open(outpu, "w+") as output_handle:
		with open(inpu) as input_handle:
			for record in SeqIO.parse(input_handle, 'fasta'):
				record.id = record.id[:40]
				SeqIO.write(record, output_handle, 'fasta')

def main():
    if len(sys.argv) == 3:
        shorten_fasta_ids(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
```

###Repeat Masking Commands:
```bash
RepeatMasker -pa 31 MaSuRCA_contigs.fasta
```
