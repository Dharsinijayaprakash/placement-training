u=int(input("Enter the range:"))
for i in range(u):
    for j in range(i):
        print(" *",end=' ')
    print()
    
while True:
    for i in range(u):
        print(" *",end=' ')
    print()
    u=u-1
    if u<=0:
        break

for i in range(u+10):
    for j in range(i):
        print()
