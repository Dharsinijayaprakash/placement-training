def gcd(u, v):
    if (u == 0):
        return v
    if (v == 0):
        return u
    if (u == v):
        return u
    if (u > v):
        return gcd(u-v, v)
    return gcd(u, v-u)
u=int(input("Enter the 1st number: "))
v=int(input("Enter the 2nd  number: "))
if(gcd(u, v)):
    print('GCD of', u, 'and', v, 'is', gcd(u, v))
else:
    print('not found')
