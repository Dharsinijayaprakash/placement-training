from numpy import *
def Transpose_matrix(org):
    row,col=org.shape
    trans=zeros((row,col),dtype=org.dtype)    
    for i in range(row):
        for j in range(col):
            trans[i][j]=org[j][i]
    return trans        
u=int(input("enter the row :"))
v=int(input("enter the column :"))
lst=[]
for i in range(u):
    ro=[]
    for j in range(v):
        r=int(input(f"enter the matrix value ({i},{j}) : "))
        ro.append(r)
    lst.append(ro)
org_matrix=array(lst)
print(f" the given matrix :\n{org_matrix}\n")
print(f"the transpose the given matrix :\n {Transpose_matrix(org_matrix)}")
