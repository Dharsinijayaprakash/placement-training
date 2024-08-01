u=int(input())
d={}
sum=0
for i in range(0,u):
    name,x,y,z=input().split()
    k=[x,y,z]
    dic[name]=w
query=input()
for i in d[query]:
    sum+=float(i)

print(format(sum/3,".2f"))
