operation=input("what calculation operation would you like to put in add,sub")

if operation=="add":
    x=int(input("how many values would you like to add"))
    sum=0
    for i in range(x):
        sum+=int(input("put in the values"))
    print(sum)

elif operation=="sub":
    x=int(input("what is the highest value"))
    y=int(input("how many values would youlike to subtract"))
    subtract=x
    for i in range(y):
        subtract-=int(input("what are the values"))
    print(subtract)



