u=int(input("Enter 1st number: "))
print(u)
v=int(input("Enter 2nd number: "))
print(v)
w=int(input("Enter 3rd number: "))
print(w)
def findgreater(u,v,w):
    if u>v and u>w:
        print(u,"Greater than ",v," and ",w)
    elif v>u and v>w:
        print(v,"Greater than ",u," and ",w)
    elif w>u and w>v:
        print(w,"Greater than ",u," and ",v)
    elif u==v and u>w:
        print(u,"and",v,"Greater than ",w)
    elif v==w and v>u:
        print(v,"and",w,"Greater than ",u)
    elif w==u and w>v:
        print(u,"and",w,"Greater than ",v)
    else:
        print("All numbers are equal")
findgreater(u,v,w)
