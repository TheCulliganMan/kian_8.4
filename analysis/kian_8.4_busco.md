#Busco
##Commands:
Just a little note, there seems to be a small Type Error in Busco 1.22.  
If --abrev goes unspecified the python dies..  It would be an easy fix, but the
workaround is just fine.
```bash
busco -f -c 10 --abrev abyss -g kian8.4k42_abyss.scaffolds.fa -l /BUSCO_v1.22/vertebrata > abyss_busco.log &
busco -f -c 10 --abrev plata -g kian8.4plat_gapClosed.fa -l /BUSCO_v1.22/vertebrata > platanus_busco.log &
busco -f -c 10 --abrev masur -g MaSuRCA_scaffold.scafSeq -l /BUSCO_v1.22/vertebrata > masurca_busco.log &
busco -f -c 10 --abrev allpa -g allpaths.final.assembly.fasta -l /BUSCO_v1.22/vertebrata > allpaths_busco.log &
busco -f -c 10 --abrev soapd -g kian8.4k29gpgenome.fa -l /BUSCO_v1.22/vertebrata > soap_busco.log &
```
##Results:
###ABYSS:
```
```
###allpaths
[Short Summary](../results/busco_stats/allpaths/short_summary_allpa)

[Full Table](../results/busco_stats/allpaths/full_table_allpa)

[Coordinates](../results/busco_stats/allpaths/coordinates_allpa)

```
Complete: 1476
Single: 1466
Multi: 10
Fragment: 818
Missing: 729
Total BUSCO groups searched: 3023
```
###Platanus:
```
```
###MaSuRCA:

[Short Summary](../results/busco_stats/masurca/short_summary_masurca)

[Full Table](../results/busco_stats/masurca/full_table_masurca)

[Coordinates](../results/busco_stats/masurca/coordinates_masurca)

```
Complete: 1055
Single: 1053
Multi: 2
Fragment: 416
Missing: 1552
Total BUSCO groups searched: 3023
```
###SOAP De Novo:
```
```
