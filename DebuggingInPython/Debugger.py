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

# Imports
from datetime import datetime, timedelta

# Acquire information from user in specific format
dob = input("What is your date of birth? (DDMMYYY)")
age_of_death = input("How old will you be when you die?")

# Convert to date object, calculate death date as date object
dob_date = datetime.strptime(dob, '%d%m%Y')
death_date = dob_date + timedelta(days=int(age_of_death) * 365)

# Calculate time left...
time_left  = death_date - datetime.now()

# Print out time left as requested.
expectancy = f"""Years left: {time_left.days / 365}
Days left: {time_left.days}
Minutes left: {time_left.days * 24 * 60}
Seconds left: {time_left.days * 24 * 60 * 60}
"""
print(expectancy)

# Save results to file
f = open("17_Exceptions_and_Debugging/output/expectancy_report.txt", "w+")
f.write(expectancy)
f.close()