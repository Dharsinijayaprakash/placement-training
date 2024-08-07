u=int(input("Number of Elements to take average of: "))  
l=[]  
for i in range(1,u+1):  
    ele = int(input("Enter the element: "))  
    l.append(ele)  
avg = sum(l)/u  
print("Average of the elements in list",round(avg,2))  
