# Liminal_Cities
SMU Data Science for Social Good Project 
## Datasets 
1. The 2021 population dataset comes from ["Annual Resident Population Estimates for Metropolitan and Micropolitan Statistical Areas and Their Geographic Components for the United States: April 1, 2020 to July 1, 2022 (CBSA-EST2022)"](https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-metro-and-micro-statistical-areas.html)
2. Shapefiles for the states and CBSAs come from the American Census Bureau wesite under ["Metropolitan and Micropolitan Statistical Areas and Related Statistical Areas"](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html) and 
3. The dataset for commuting flow comes directly from the [LEDH](https://lehd.ces.census.gov/data/#lodes) website. It is retrieved directly from the website in the .ipynb file.
4. The dataset for state location crosswalks also from the from LEDH website via direct retrieval.
## Methods
1. Using dataset for 2021 CBSA populations, we removed entires designated as "county". 
2. Many metopolitan areas include multiple distinct cities.
3. LODES commuting location data not available for Massachusets and New Hampshire. 
4. 2020 LODES data not available for AK, AR, MS, so data from 2018 (AR,MS) and 2016 (AK) was used.   
