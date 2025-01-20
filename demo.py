import requests 
# requests will let me get the API from IPUMS
import pandas as pd
from datetime import datetime

# IPUMS API
token = "59cba10d8a5da536fc06b59d2599cf654a2b4a778739cbe6644d6e0e"

# /crosswalks/
# attempt 1: https://api.ipums.org/supplemental-data/crosswalks/ 
# /blocks-1980/
# /estimates/

# summary statistics by county from 1980 to 2020 with harmonized 
# geographic boundaries for census blocks

baseurl = "https://api.ipums.org/metadata/nhgis/datasets?version=2"

pop_housing = "1960_tPH"

# f = interpolated string

baseurl_individual = f"https://api.ipums.org/metadata/nhgis/datasets/{pop_housing}?version=2"

headers = {
    "Authorization": f"Bearer {token}"  # Replace "Bearer" with the scheme required by the API, if any
}

# geogLevels
# dataTables

try:
    # Make a GET request
    response = requests.get(baseurl_individual, headers=headers)
   
    # Raise an error if the request was unsuccessful
    response.raise_for_status()
   
    # Parse the JSON response
    json_data = response.json()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Format: YYYYMMDD_HHMMSS
    df_geo = pd.DataFrame(json_data["geogLevels"])
    df_data = pd.DataFrame(json_data["dataTables"])
    df_geo.to_excel(f"{pop_housing}_geo1960tPH_{timestamp}.xlsx", index=False)
    df_data.to_excel(f"{pop_housing}_data1960tPH_{timestamp}.xlsx", index=False)

    print("success")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")