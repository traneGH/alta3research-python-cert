# alta3research-python-cert (Alt3 Research Certification Project)

My goal is practing the below topics:
 - request API, Regex, Crayons, OOPs (Class), Try/Exception, Collections (List, Dictionary), write to json/csv files


Project Description: 
Asteroids - NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information
Collect a list of Asteroids based on their closest approach date to Earth within 6 days:
- Collect the data from Neo - Feed's API.  
- Passing the Start date and End Date and generate the output files, and will be saved under "files" folder
- Store the response in JSON format into a file. File name pattern is "<start date>_<end date>_asteroid_info.json"  
- Stored these data "Name, URL, Potential Hazardous Asteroid" into the csv file for each date. File name pattern is "asteroid_info_<specific date within the range from start to end date>.csv"
- Either use the register API key or use "DEMO_KEY".  DEMO_KEY has limited access

Feed API's URL:
GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY

Sample URL:
https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-06-15&end_date=2022-06-20&api_key=sXCrRvnqYpg0JfhUrTFY4h4DTVUUdHpyRNPxLbCy 

 
## Getting Started

This is the main script to run this program
python3 .\alta3research-pythoncert01.py 

### Prerequisites

Needed to install the below:

python3 -m pip install requests
python3 -m pip install crayons

Make sure the "files" folder is created 

## Built With

* [Python](https://www.python.org/) - The coding language used

## Authors

* **Elizabeth Ngoc Tran** - *Initial work* - [YourWebsite](https://example.com/)

