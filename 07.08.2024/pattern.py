def myfunc(u):
    v=u-1
    for i in range(0, u):
        for j in range(0, v):
            print(end=" ")
        v=v-1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
u=int(input("Enter the number: "))
myfunc(u)
