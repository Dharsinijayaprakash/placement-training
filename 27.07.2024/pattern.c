#include <stdio.h>
 int main()
{
    int u= 5, k, l, v = 1, w;
    w= u - 1;
    for (l = 1; l <= u; l++)
      {
      v= l;
      for (k= 1; k<=w; k++)
      printf(" ");
      w--;
      for (k = 1; k <= l; k++) {
            printf("%d", v);
            v++;
        }
        v--;
        v--;
        for (k = 1; k < l; k++) {
            printf("%d", v);
            v--;
        }
          printf("\n");
    }
    return 0;
}
