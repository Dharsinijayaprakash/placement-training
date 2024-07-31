#include<stdio.h>
    int main(){
        float p,r,t,i;
        printf("Enter principal,rate and time: ");
        scanf("%f %f %f",&p,&r,&t);
        i=(p*r*t)/100;
        printf("Simple Interest: %.2f\n",i);
        }
    
