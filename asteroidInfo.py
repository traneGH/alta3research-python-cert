#!/usr/bin/python3

class Asteroids:
    def __init__(self, startDate):
        self.start_date = startDate
        self.asteroidList = []

    def get_start_date(self):  
        return self.start_date

    def getAsteroidList(self):
        # creating list	
        return self.asteroidList

    def display(self):
        for each in self.asteroidList :
            print(each)

    def getDataLabelList(self) :
        return ["Name", "URL", "Potential Hazardous Asteroid"]

    def appendToAsteroidList(self, asteroidObj) :
        self.asteroidList.append(asteroidObj.getDataList())
    
class Asteroid:
    def __init__(self, asteroidName, urlName, isHazardous):
        self.asteroidName = asteroidName
        self.nasaURL = urlName
        self.isHazardous = isHazardous
       
    def getIsHazrdous(self) :
        return self.isHazardous
    
    def getAsteroidName(self) :
        return self.asteroidName

    def getNasaURL(self):
        return self.nasaURL

    def getDataList(self) :
        return [self.getAsteroidName(), self.getNasaURL(),self.getIsHazrdous()]
     