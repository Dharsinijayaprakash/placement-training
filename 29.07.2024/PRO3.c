#include<stdio.h>
Int main()
{
  int n,r,c,i,j,k,max_value=0,count-0;
  scanf("%d",&n);
  int grid[101][101]={0};
  for(i=0;i<n;i++)
    {
      scanf("%d %d",&r,&c);
      for(j=1;j<=r;j++)
        {
          for(int k=1;k<=c;k++)
            {
              grid[j][k]++;
              if(grid[j][k]>max_value)
              {
                max_value=grid[j][k];
                count=1;
              }
              else if(grid[j][k]==max_value)
              {
                count++'
              }
            }
        }
    }
  print("%d\n",count);
  return 0;
}
