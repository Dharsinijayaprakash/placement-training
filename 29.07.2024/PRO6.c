#include<stdio.h>
int main()
{
   int ph,nh, m, m1;
  printf("Enter time in hours: ");
  scanf("%d",&ph);
  nh=(ph+1)%12;
  m1=ph*60;
  m=(nh*60)/11;
  if(ph>=1)
{ 
printf("(%d/11)\n",m1);
}
else
  {
printf("Invalid input\n");
 }
}
