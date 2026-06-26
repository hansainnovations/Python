# don't change the code below line
age = input("Enter your current age : ")
# don't change the code above line

# Write your code below this line
your_age = int(age)
year_left = 100 - your_age
month_left = year_left * 12
weeks_left = year_left * 52
days_left = year_left * 365

message = f"You have {year_left} Years, {month_left} Months, {weeks_left} Weeks and {days_left} Days left"

print("\n")
print(message)
