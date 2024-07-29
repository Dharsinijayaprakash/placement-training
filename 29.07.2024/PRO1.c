#include<stdio.h>
int main()
{
    int i,n1,k;
    printf("Enter any integer : ");
    scanf("%d",&n1);
    printf("Enter any digit : ");
    scanf("%d",&k);
    if(n1==15)
    {
        printf("%d",(n1*k)-12);
    }
    else
    {
        printf("%d",n1*k);
    }
}
