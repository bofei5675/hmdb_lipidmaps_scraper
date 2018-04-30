# Scraper for LIPIPMAPS ID in hmdb

Since hmdb hinds their LIPIDMAPS ID inside their source file, we decided to grab this by web crawler. This script will go about one week to grab all LIPIDMAPS ID it can find by crawl all metabolites website.

Prerequesite:
* Python 3.5
* Package such as urlib,bs4,pandas,sqlalchemy
* RaMP database installed (or you need to have all hmdb metabolites ID to looking at single websites)

Update at 4/30/2018
Then, about 5000 metabolites have LIMPIDMAPS ID, and they are imported to RaMP.

### Run the script to get lipidmaps id
1. Run web crawler in script hmdb_lipidmaps.py to grab all ids (takes about 1 week)
2. Filter out duplicates and NA returned by crawler
3. Run the script in uploadLPid.py to import the filtered metabolites ID into RaMP


### Author
Bofei Zhang (zhang.5675@osu.edu)
