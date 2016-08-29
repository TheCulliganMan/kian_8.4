#Busco
##Commands:
I ran all the commands in a docker image.  It can be found on the docker hub.
```bash
docker run -itv <path>:/work theculliganman/busco
```
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
###Abyss:
```
Complete: 1629
Single: 1620
Multi: 9
Fragment: 755
Missing: 639
Total BUSCO groups searched: 3023
```

[Short Summary](../results/busco_stats/abyss/short_summary_abyss)

[Full Table](../results/busco_stats/abyss/full_table_abyss)

[Coordinates](../results/busco_stats/abyss/coordinates_abyss)

###Allpaths:
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
[Short Summary](../results/busco_stats/platanus/short_summary_plata)

[Full Table](../results/busco_stats/platanus/full_table_plata)

[Coordinates](../results/busco_stats/platanus/coordinates_plata)

```
Complete: 1135
Single: 1125
Multi: 10
Fragment: 811
Missing: 1077
Total BUSCO groups searched: 3023
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
###Soap De Novo:
[Short Summary](../results/busco_stats/soap/short_summary_soapd)

[Full Table](../results/busco_stats/soap/full_table_soapd)

[Coordinates](../results/busco_stats/soap/coordinates_soapd)
```
Complete: 1885
Single: 1807
Multi: 78
Fragment: 780
Missing: 358
Total BUSCO groups searched: 3023
```
