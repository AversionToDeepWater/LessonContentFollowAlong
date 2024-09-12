'''
__ Time Left to Live __

Take a users input, in date format, of their date of birth (DDMMYYYY).
Then take that users life expectancy.

Provide them with the dire news of how long they have left to live.

Provide the news in the format of;
- First: Years left to live
- Second: Minutes left to live
- Third: Seconds left to live

### OPTIONAL ###
Write the life expectancy report to a text file.

'''
from datetime import datetime

user_dob = str(input("Please input your date of birth in DDMMYYYY format: "))
life_expectancy = int(input("Please input your life expectancy: "))

datetime_dob = datetime.strptime(user_dob,"%d%m%Y")




