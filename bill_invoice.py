print("WELCOME TO THE TIP CALCULATOR")

Totalbill=float(input("what was the total bill?"))

percentagetip=input("what was the percentage tip you ould like to give? [10,12 or 15]?\n")

people=input("how many people to split the bill?")
tip=int(Totalbill)*int(percentagetip)/100
eachperson=int(Totalbill)+int(tip)/int(people)
print(eachperson)
