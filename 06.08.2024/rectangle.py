def area(u,v):
    return u*v
def perimeter(u,v):
    return 2 * (u + v)
u = float(input("Enter the length of the rectangle: "))
v = float(input("Enter the width of the rectangle: "))
w = int(input("Enter ur choice: {1 for area},{2 for perimeter}"))
if w==1:
    print("The area is:",area(u,v))
elif w==2:
    print("The perimeter is:",perimeter(u,v))
