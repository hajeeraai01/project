
#include<stdio.h>
struct structure
{
    float myvalue;
    char myletter;
};
    void use()
{
    struct structure s1;
     s1.myvalue=15.5;
     s1.myletter='A';
      printf("\n myvalue is: %f",s1.myvalue);
      printf(" \n myletter is: %c",s1.myletter);
      return 0;
}


