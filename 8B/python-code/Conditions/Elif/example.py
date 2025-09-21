number = 8

if number < 0:
    category = "Negative"
elif number == 0:
    category = "Zero"
elif number % 2 == 0:
    category = "Even"
else:
       category = "Odd"

print("The number belongs to the category:", category)
   