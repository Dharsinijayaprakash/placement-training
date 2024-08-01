if __name__ == '__main__':
    u = int(input())
    v = int(input())
    w = int(input())
    a = int(input())
    lst=[[i,j,k]for i in range(u+1)for j in range(v+1)for k in range(w+1)if i+j+k !=a]
    print(lst)
