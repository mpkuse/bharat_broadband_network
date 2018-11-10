# BharatNet.

Program of the government to connect villages of India with fiber-optic cable. List of villages where currently available (150k villages as of Nov. 2018)
To know more on the government's plan you might want to look at the [wiki page](https://en.wikipedia.org/wiki/Bharat_Broadband_Network).



[CSV file](0_337.csv) of the pdf. The CSV is cleaned and inspected manually. It is ready for analysis/visualization.
[Original PDF](http://www.bbnl.nic.in/WriteReadData/LINKS/List_GPs_Fbr_Blck6253a7e4-366d-41ac-89fc-9fd94d047763.pdf)

hope it helps.


## How I converted the PDF?
Since the numerous PDF-to-csv have a page limit and this file was 337 pages, I was out of luck.
I used [tabula-py](https://github.com/tabulapdf/tabula-java).

Only a handful of the items had to be managed manually.

```
import tabula
tabula.convert_into( 'List_GPs_Fbr_Blck6253a7e4-366d-41ac-89fc-9fd94d047763.pdf', 'List.csv', pages='1-337' )
```
