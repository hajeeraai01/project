#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=15, b=30;
    printf("value of a   :%d \t\n",a);
    printf("address of a :%d \n",&a);
    printf("----------\n");
    printf("value of b   :%d \t\n",b);
    printf("address of b :%d \n",&b);
    printf("----------\n");


    int *p=&a;
    printf("value of p                        :%d\t\n",p);
    printf("address of p                      :%d\t\n",&p);
    printf("value stored in the address of p  :%d\t\n",*p);
    printf("----------\n");


    int **r=&q;
    printf("value of r                                           :%d\t\n",r);
    printf("address of r                                         :%d\t\n",&r);
    printf("value stored in the address of q in the address of p :%d\t\n",**r);

    void *s=&a;
    printf("value s                                                                   :%d\t\n",s);
    printf("address of s                                                              :%d\t\n",&s);
    printf("value stored in the address of  r to the address of q in the address of p :%d\t\n",*(int*)s);

    return 0;
}
