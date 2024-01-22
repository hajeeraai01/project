#include<stdio.h>
int each()
{
addition1(getb(), geta());
subtraction2(getb(), geta());
divide3(getb(),geta());
return 0;
}


int geta()
{
int a;
    printf("\n enter the value a");
    scanf("%d",&a);
    return a;
}
int getb()
{
    int b;
    printf("\n enter the value b");
    scanf("%d",&b);
    return b;

}
int addition1( int a, int b)

{

int c;
c=a+b;



        printf("\n add the value  a+b %d \n",c);

        return 0;

    }
    int subtraction2 (int a, int b)
    {
        int c;
      c=a-b;
        printf("\n subtract the value a-b %d \n",c);
        return 0;

    }
    int divide3(int a, int b)
    {

        int c;
        c=a/b;
        printf("\n divide the value a/b %f \n",c);
        return 0;
    }




