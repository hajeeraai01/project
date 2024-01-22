#include<stdio.h>
int main()
{
    int a;
    printf( "enter the value is a=");
    scanf("%d",&a);
    if(a % 2 == 0)
    {
        printf("Even number");
    }
   else
    {
        printf("odd number");
    }
    return 0;
}