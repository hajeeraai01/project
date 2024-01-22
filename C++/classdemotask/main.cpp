
#include <iostream>

using namespace std;

class operatorclass
{
public :
    int op = 1 ;
    void add()
    {
        int a , b ;
        cout << "\nA:" ;
        cin >> a ;
        cout << "B:" ;
        cin >> b ;
        cout << "Add:" << (a+b) ;
    }
     int sub()
    {
        int a , b ;
        cout << "\nA:" ;
        cin >> a ;
        cout << "B:" ;
        cin >> b ;
        cout << "Sub:" << (a-b) ;
    }
    void multiply()
    {
        int a , b ;
        cout << "\nA:" ;
        cin >> a ;
        cout << "B:" ;
        cin >> b ;
        cout << "Multiply:" << (a*b) ;
    }
    int div()
    {
        int a , b ;
        cout << "\nA:" ;
        cin >> a ;
        cout << "B:" ;
        cin >> b ;
        cout << "Div:" << (a/b) ;
    }
    void modls();
    void increment();
    void decrement();

};
void operatorclass::modls()
{
        int a , b ;
        cout << "\nA:" ;
        cin >> a ;
        cout << "B:" ;
        cin >> b ;
        cout << "Modulus:" << (a%b) ;
}
void operatorclass::increment()
{
        int a ,c ;
        cout << "\nA:" ;
        cin >> a ;
        c=a++ ;
        cout << "Increment:" << a++ ;
}
void  operatorclass::decrement()
 {
        int a , c ;
        cout << "\nA:" ;
        cin >> a ;
        c=a-- ;
        cout << "Decrement:" << a-- ;
}
int main()
{
    operatorclass opc;
    cout << opc.op;
    opc.add();
    opc.sub();
    opc.multiply();
    opc.div();
    opc.modls();
    opc.increment();
    opc.decrement();
    return 0;
}


