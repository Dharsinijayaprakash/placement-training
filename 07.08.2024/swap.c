#include <stdio.h>
int main()
{
  int u = 10;
  int v = 20;
  printf("u: %d , v: %d\n", u, v);
    u = u + v;
    v = u - v;
    u = u - v;
  printf("u: %d , v: %d\n", u, v);
  return 0;
}
