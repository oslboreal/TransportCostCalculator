from enum import Enum
# Representation of the Weekdays.s
class Day(Enum):
        MON = 0
        TUE = 1
        WED = 2
        THU = 3
        FRI = 4
        #SAT = 5
        #SUN = 6

# Geting the name of the weekday.
#print(Day(0).name)

import datetime
from calendar import monthrange
import json
from pprint import pprint

# This class represents the pattern used to set the cost of the day.
class Pattern:
    dictionary = {
		Day.MON.name : 0.0,
		Day.TUE.name : 0.0,
		Day.WED.name : 0.0,
		Day.THU.name : 0.0,
		Day.FRI.name : 0.0
       #Day.SAT.name : 0.0,
       #Day.SUN.name : 0.0
	}
    data = {}

    def __init__(self):
        data_file = open('data.json', 'r')  
        self.data = json.load(data_file)

    def updateCosts(self):
        for day in self.data["days"]:
            self.dictionary[day['name']] = day['cost']

class Manager:
    datetime = datetime.datetime.today()
    weekday = datetime.weekday()
    dayname = Day(weekday).name
    year = datetime.year
    month = datetime.month
    monthDays = monthrange(year, month)[1]
    pattern = Pattern()
    weekCost = float("0.0")
    businessDays = 0

    def __init__(self):
        self.pattern.updateCosts()
        self.calculateBusinessDays()

    def calculateBusinessDays(self):
        i = 1
        while i <= self.monthDays:
            wday = datetime.datetime(self.year, self.month, i).weekday()
            if Manager.isBusinessDay(wday):
                self.businessDays += 1
            i += 1

    def isBusinessDay(value):
        if value == 0 or value == 1 or value == 2 or value == 3 or value == 4:
            return True
        else:
            return False

    def calculateMonth(self):
        weekCost = float("0.0")
        
        for var in self.pattern.dictionary:
            weekCost = weekCost + float(self.pattern.dictionary[var])
            
        self.weekCost = weekCost



manager = Manager()
manager.calculateMonth()

print("-- Gasto semanal de transporte:")
print((manager.businessDays / 5) * manager.weekCost)
a = input()