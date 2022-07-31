#!/usr/bin/python3
'''
Elizabeth Ngoc Tran | Alta3Research 

Project Description: 
Collect a list of Asteroids based on their closest approach date to Earth within 6 days:
- Collect the data from Neo - Feed's API.  
- Passing the Start date and End Date and generate the output files, and will be saved under "files" folder
- Store the response in JSON format into a file. File name pattern is "<start date>_<end date>_asteroid_info.json"  
- Stored these data "Name, URL, Potential Hazardous Asteroid" into the csv file for each date. 
  File name pattern is "asteroid_info_<specific date within the range from start to end date>.csv"

Sample URL:
https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-06-15&end_date=2022-06-20&api_key=sXCrRvnqYpg0JfhUrTFY4h4DTVUUdHpyRNPxLbCy 

'''
import requests
import json
import re
import crayons 
import csv  # importing the csv module 

from webbrowser import get
from datetime import datetime as dt
from asteroidInfo import Asteroid  
from asteroidInfo import Asteroids
 
NEO_FEED_API = "https://api.nasa.gov/neo/rest/v1/feed"
API_KEY = "sXCrRvnqYpg0JfhUrTFY4h4DTVUUdHpyRNPxLbCy"  #Either use the register API key or use "DEMO_KEY".  DEMO_KEY has limited access. 
FILE_PATH = "files/"   # for output files

FULL_OUTPUT_JSONFILE="asteroid_info.json"

# Compare date different between End date and Start date
def getDayDiff(startDate, endDate) : 
  res = (dt.strptime(endDate, "%Y-%m-%d") - dt.strptime(startDate, "%Y-%m-%d")).days
  return res

# Request HTTP get data and response as a dictionary
def getResponseNearEarthObjects(startDate, endDate):
  gotresp = requests.get(f"{NEO_FEED_API}?start_date={startDate}&end_date={endDate}&api_key={API_KEY}")  # Send HTTP GET
  resultDic = gotresp.json().get("near_earth_objects")
  return resultDic

# Write response data into json file
def writeAllDataToJsonFile(startDate, endDate, jsonResp):
  # open a file we write our data into
  outputJsonFile = FILE_PATH + startDate+"_"+endDate+"_"+FULL_OUTPUT_JSONFILE
  with open(outputJsonFile, "w") as asteroidfile:
    print(f"\n{crayons.blue('Write full data from')} {crayons.blue(startDate)} to {crayons.blue(endDate)} {crayons.blue('to json file:')} {crayons.blue(outputJsonFile)}")
    json.dump(jsonResp, asteroidfile)

# Write data based on start date into csv file, passing the response JSON data as in dictionary type
def writeAsteroidsDataToCSVFiles(asteroidDic):
  for eachDate in sorted(asteroidDic.keys()):  # sorted by date
    asteroidsObj = createSelectedAsteroidListByDate(asteroidDic, eachDate)  
    # field names 
    fields = asteroidsObj.getDataLabelList()
    # data rows of csv file 
    rows = asteroidsObj.getAsteroidList()
     
    # name of csv file 
    fileName = FILE_PATH+"asteroid_info_" + eachDate + ".csv"
        # writing to csv file 
    with open(fileName, 'w', encoding='UTF8', newline='') as csvfile:  #save each line into csv file without extra blank row
      try:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)   
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        csvwriter.writerows(rows)
        print(f"{crayons.blue('Start Date:')} {crayons.red(eachDate)} - {crayons.blue('write data into this file')} {crayons.red(filename)}")
      except Exception as err:
        print("Error - ", err)


# Build the list of Asteroid objects
def createSelectedAsteroidListByDate(dataDic, eachDate) : 
  asteroidsObj = Asteroids(eachDate)
  for eachElt in dataDic.get(eachDate):   
    asteroidObj = Asteroid(eachElt.get('name'), eachElt.get('nasa_jpl_url'), str(eachElt.get('is_potentially_hazardous_asteroid')))
    asteroidsObj.appendToAsteroidList(asteroidObj)  # append the Asteroid object into the list
  return asteroidsObj
 
# Request data from user
def getInputData():
  mylistdict = []
  startdate_input = ''
  enddate_input = ''
  while(True):
    try:
      startdate_input = input(crayons.blue("Please enter the start date in this format YYYY-MM-DD: (i.e. 2015-09-07) ",bold=True))
      enddate_input = input(crayons.blue("The end date MUST within 6 days from start date, format YYYY-MM-DD: (i.e. 2015-09-11) ",bold=True))
      numDateDiff = getDayDiff(startdate_input, enddate_input)
      if ( numDateDiff > 6):
        print(f"{crayons.red('The difference between Start date and End date is')} {crayons.red(numDateDiff)} {crayons.red('day(s). The end date MUST within 6 days from start date.')}")
        continue 

      mylistdict = {"startdate_input": startdate_input, "enddate_input": enddate_input}
      startdate_input = mylistdict["startdate_input"]
      enddate_input = mylistdict["enddate_input"]

      matchStartDate = re.search(r'\d{4}-\d{2}-\d{2}', startdate_input)
      matchEndDate = re.search(r'\d{4}-\d{2}-\d{2}', enddate_input)
        
      # checking if correct format date
      if ( matchStartDate and matchEndDate) :
        keep_going = input(crayons.blue("\nWould you like to re-enter the date? Enter any key for 'Yes, enter 'n' for 'No' : ", bold=True))
        if (keep_going.lower() == 'n'):
          break
        else:
          continue
      else:
        print(crayons.red("Please input correct date format."))
        continue 
    except Exception as err:
      print("Error in input value - ", err)
  return startdate_input,enddate_input

# Main business logic
def main():
  print('Calling main ...')
  # collect string inputs from the user
  startdate_input, enddate_input = getInputData() 
  resultDataDic = getResponseNearEarthObjects(startdate_input, enddate_input)  #Response JSON data as in dictionary type
  writeAllDataToJsonFile(startdate_input, enddate_input, resultDataDic) 
  writeAsteroidsDataToCSVFiles(resultDataDic)
  
# This condition specifies that the main() function will only be called if this script is run directly 
# (not imported elsewhere)
if __name__ == "__main__" :
  main()