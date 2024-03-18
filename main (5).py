input_date = input("Please enter the date 'YYYY-MM-DD': ")

year, month, day = input_date.split('-')

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

if int(year) <= MIN_YEAR: 
    validDate = False
if int(month) < MIN_MONTH or int(month) > MAX_MONTH:
    validDate = False
if int(day) < MIN_DAY or int(day) > MAX_DAY:
    validDate = False

  
    output = f"The date {month}/{day}/{year} is a valid date."
else:
    output = f"The date {month}/{day}/{year} is an invalid date."

print(output)