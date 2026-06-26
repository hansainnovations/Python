# Do not change the code below
two_digit_number = input("Type a two digit number: ")
# Do not change the code above
# Write your code below this line 

# Get the number at unit place and tenth place using substring then converting it to int

ten_place = int(two_digit_number[0])
unit_place = int(two_digit_number[1])

# Add the Two numbers 

new_number = ten_place + unit_place

print("\n")
print(new_number)