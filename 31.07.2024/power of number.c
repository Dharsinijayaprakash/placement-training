#include<stdio.h>
    int power(int b,int e){
        if(e==0)
            return 1;
        else
            return b*power(b,e-1);
    }

    int main(){
        int b,e;
        printf("Enter base and exponent: ");
        scanf("%d %d",&b,&e);

        printf("%d^%d=%d\n",b,e,power(b,e));
       
    }
