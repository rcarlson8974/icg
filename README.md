# pdf-report-generator

Generates an excel (csv) report for each pdf file



```
~/projects/foo/some-project-dir:master ✗ ➭ ./bin/pdf-report-generator.py
Generating PDF Report.........

Processing PDF A3.1-First-Floor-Plan-Rev.0.pdf
Page:Word Count for Quartz is ['Quartz', '0', '0']
Sentences for Quartz is
Page:Word Count for Granite is ['Granite', '0', '0']
Sentences for Granite is
Page:Word Count for Aluminum is ['Aluminum', '1', '1']
Sentences for Aluminum is Aluminum brake metal window sill

Page:Word Count for Concrete is ['Concrete', '1', '1']
Sentences for Concrete is Concrete floor, slope to drain; separate pour at each

Page:Word Count for TMI is ['TMI', '0', '0']
Sentences for TMI is
Page:Word Count for Case Systems is ['Case Systems', '0', '0']
Sentences for Case Systems is
Page:Word Count for Leedo is ['Leedo', '0', '0']
Sentences for Leedo is
Page:Word Count for Saco is ['Saco', '0', '0']
Sentences for Saco is

.......

Processing PDF A6.1-Building-Sections-Rev.0.pdf
Page:Word Count for Quartz is ['Quartz', '0', '0']
Sentences for Quartz is
Page:Word Count for Granite is ['Granite', '0', '0']
Sentences for Granite is
Done processing PDF A3.6-Enlarged-Floor-Plans-Rev.0.pdf

Done Generating PDF Report.........
```

Sample output (csv)
```
Project Name:,A1.1-Site-Plan-Rev.0.pdf
Customer:,ACME Contracting
,
,
Key Words,Page,Count,Sentence(s)
Materials
Quartz,0,0,
Granite,0,0,
Aluminum,0,0,
Concrete,1,7,"Concrete sidewalk, see Civil drawings; see Detail Boo
Concrete patio; see Civil drawings for slopes        
Concrete curb and gutter; see Civil drawings         
Concrete curb adjacent to stoop, eliminate gutter por
Concrete pavement with stoop, see Details and Structu
Concrete slab, slope 1/8"" per foot to drain out doors
Concrete pad with artificial turf
"
,
Competitors
TMI,0,0,
Case Systems,0,0,
Leedo,0,0,
Saco,0,0,
Hansen Company,0,0,
ACG,0,0,
Wilkie,0,0,
Randawg Corp,0,0,
,
Characteristics
Face Frame,0,0,
PLAM,0,0,
Cabinet,0,0,
Countertop,0,0,
Casework,0,0,
Millwork,0,0,
Woodworking,0,0,
```