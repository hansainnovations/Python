# Don't change the code below line
num = int(input("Enter a number value: "))
# Don't change the code above line
# Write your code below this line
if num >= 0 and num <= 9:
  print('Number is a "Single" digit')
elif num >=10 and num <= 99:
  print('Number is a "Double" digit')
else:
  print('Number is a "Neither Single Nor Double" digit')