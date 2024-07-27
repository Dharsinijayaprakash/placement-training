def pyramid(u):
    for i in range(u, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
u=int(input("Enter the range:"))
pyramid(u)
