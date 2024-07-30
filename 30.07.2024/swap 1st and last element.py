u=int(input())
v=[]
for i in range(u):
    w=int(input())
    v.append(w)
print("Interchanging first and last element")
temp=v[0]
v[0]=v[-1]
v[-1]=temp
