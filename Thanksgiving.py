Turkey_Day = input("When was the First Turkey Day game played?: ")
while Turkey_Day == 1907:
    print(Turkey_Day)
total = 0
for i in range(6):
    next = int(input("enter a number: "))
    if next < 1907:
        print("correct")
        break
    print("Incorrect!")