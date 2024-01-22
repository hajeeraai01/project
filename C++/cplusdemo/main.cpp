#include <iostream>

using namespace std;

int main()

{
    int value1,value2,total,op;
    cout<<"enter value1";
    cin>>value1;
    cout<<"enter value2";
    cin>>value2;
    cout<<"enter operator";
    cin>>op;
    switch(op)
   {

    case 1:
        total=value1+value2;
    cout<<"added value of a and b"<<total;
    break;

    case 2:
        total=value1-value2;
        cout<<"subtract value of a and b"<<total;
        break;
    case 3:
        total=value1*value2;
        cout<<"multiply value of a and b"<<total;
        break;
    case 4:
        total=value1/value2;
        cout<<"divition value of a and b"<<total;
        break;
    case 5:
        total=value1%value2;
        cout<<"modulus value of a and b"<<total;
        break;
    case 6:
        value1++;
        value2++;
        cout<<"increment value of a and b"<<value1<<value2;
        break;
    case 7:
        value1--;
        value2--;
        cout<<"increment value of a and b"<<value1<<value2;
        break;
    case 8:
        value1+=2;
        value2+=1;
        cout<< "add assign values:"<<value1<<end1;
        break;

}
}


