u = int(input())
for i in range(u):
    v = int(input())
    x = set(map(int,input().strip().split()))
    w = int(input())
    y = set(map(int,input().strip().split()))
    if x.issubset(y):
        print (True)
    else:
        print (False)
