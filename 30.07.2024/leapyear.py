def leap(v):
  if (v%400==0) or (v%100!=0) and (v%4==0):
    print("Its leap yera")
  else:
    print("Its not a leap year")
u=int(input("Enter the year:"))
leap(u)
