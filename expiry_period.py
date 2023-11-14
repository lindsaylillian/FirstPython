
currentage=input("what is the current age\n?")

finalage=input("what is the expected age?")

#calculates the years left
yearsleft=int(finalage)-int(currentage)

#calculates the months left 
monthsleft=int(yearsleft*12)

#calculates the days left 
daysleft=int(monthsleft*365)
print(f"you have{yearsleft} years left,{monthsleft} months and,{daysleft}daysleft")

