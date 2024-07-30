u=int(input())
v=[]
for i in range(u):
    w=int(input())
    v.append(w)
for i in range(u):
    for j in range(i+1,u):
        if v[i]<v[j]:
            temp=v[i]
            v[i]=v[j]
            v[j]=temp
print(v)
