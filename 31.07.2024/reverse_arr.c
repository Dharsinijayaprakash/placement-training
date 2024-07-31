#include<stdio.h>
    void reverseArray(int a[],int s,int e){
        while(s<e){
            int temp=a[start];
            arr[s]=arr[e];
            arr[e]=temp;
            s++;
            e--;
        }
    }

    int main(){
        int a[]={1,2,3,4,5};
        int size=sizeof(a)/sizeof(a[0]);

        reverseArray(a,0,size-1);

        printf("Reversed array: ");
        for(int i=0;i<size;i++){
            printf("%d ",a[i]);
        }
        printf("\n");

    }
