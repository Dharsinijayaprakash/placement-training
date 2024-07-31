 #include<stdio.h>
    int main(){
        int u,i,flag=0;
        printf("Enter a number: ");
        scanf("%d",&u);
        if(u<=1){
            printf("Not a prime number.\n");
            return 0;
        }

        for(i=2;i<=u/2;i++){
            if(u%i==0){
                flag=1;
                break;
            }
        }
        if(flag==0){
            printf("Prime number.\n");
        }else{
            printf("Not a prime number.\n");
        }
    }
