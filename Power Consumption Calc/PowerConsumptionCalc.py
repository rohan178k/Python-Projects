units = int(input("Enter number of units of power consumption: "))
rate = 0

if units >= 0 and units <= 50:
    rate = 3
elif units >= 51 and units <= 100:
    rate = 6
elif units >= 101 and units <= 150:
    rate = 9
elif units >= 151 and units <= 200:
    rate = 12
elif units >= 201:
    rate = 15
else:
    print("Invalid Input!")


bill = rate*units
print("Power consumption: ", units, " units")
print("Rate per unit: ", rate)
print("Total bill: ", bill)
