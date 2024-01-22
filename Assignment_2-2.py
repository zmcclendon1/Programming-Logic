""" 
Assign an integer variable named myCurrentAge with your current age in years.
Assign an integer variable named currentYear with the value of the current year. Use four digits for the year.
Execute the program and ensure the output is correct.


PSEUDOCODE: CALCULATE AGE IN YEAR X

currentAge = 20
currentYear = 2024
start(year)
    yearsFrom = year - currentYear
    ageInYear = yearsFrom + currentAge
    output ageInYear
end

"""
#HOUSEKEEPING
myCurrentAge = 20
currentYear = 2024


def calculateAgeFromYear(year):
    yearsFrom = year - currentYear
    myNewAge = yearsFrom + myCurrentAge
    print("I will be " + str(myNewAge) + " in " + str(year) + ".")

calculateAgeFromYear(2050)
