#include<stdio.h>
    int main(){
        int u,sum=0;
        printf("Enter a number: ");
        scanf("%d",&u);

        while(u!=0){
            sum+=u%10;
            u/=10;
        }
        printf("Sum of digits: %d\n",sum);
	 }
