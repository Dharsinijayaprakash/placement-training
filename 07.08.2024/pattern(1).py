def myfunc(u):
    for i in range(0, u):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

u=int(input("Enter the range: ))
myfunc(u)
