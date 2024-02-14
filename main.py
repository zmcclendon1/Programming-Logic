# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Get the year, then the month, then the day
getYear = input("Year: ")
getMonth = input("Month: ")
getDay = input("Day: ")
# housekeeping()
year = int(getYear)
month = int(getMonth)
day = int(getDay)
# Check to be sure date is valid
if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not
"""
month = 5 
day = 32
year = 2014

month = 2
day = 29
year = 1936

month = 11
day = 31
year = 1873
"""
# End of Job
if validDate == True:
    print(f"{month}/{day}/{year} is a valid date")
else:
    print(f"{month}/{day}/{year} is an invalid date")