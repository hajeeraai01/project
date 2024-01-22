#include <iostream>

using namespace std;

class result
{
public :
    int sum( int a , int b)
    {
        int c;
        c=a+b;
        cout << "total:" << c;
    }
    float sum( float a , float b , float c )
    {
        float d;
        d=a+b+c;
        cout << "\t total:" << d;
    }
};

int main()
{
    result rs;
    int m1,m2;
    cin >> m1 >> m2 ;
    rs.sum(m1,m2);
    float a,b,c;
    cin >> a >> b >> c ;
    rs.sum(a,b,c);
    return 0;
}

/*
#include <iostream>
using namespace std;
class result
{
public :
    result()
    {
        int a ;
        cout << "First Mark:";
        cin >> a;
        if (a>=35)
        {
            cout << "Pass" ;
        }
        else
        {
            cout << "Fail" ;
        }
    }
    result( int a )
    {
        if( a>=35)
        {
            cout << "Good" ;
        }
        else
        {
            cout << "Bad" ;
        }
    }
    void marks( int a )
    {
        if (a>=35)
        {
            cout << "Pass" ;
        }
        else
        {
            cout << "Fail" ;
        }
    }
};
int main()
{
    result rs;
    int a ;
    cout << "\nFirst mark remarks:";
    cin >> a;
    result rs1(a);
    //rs.marks(a);
    return 0;
}
*/
/*
#include <iostream>
using namespace std;
class result
{
public :
    void marks( int a )
    {
        if (a>=35)
        {
            cout << "Pass" ;
        }
        else
        {
            cout << "Fail" ;
        }
    }
};
int main()
{
    int a;
    result rs;
    cout << "value in a :";
    cin >> a;
    rs.marks(a);
    return 0;
}
*/
/*
#include <iostream>
using namespace std;
class result
{
public :
    int a;
};
int main()
{
    cout << "value in a :";
    result rs;
    cin >> rs.a;
    cout << "\t rs value in a :" << rs.a;
    rs.a = 35;
    cout << "\n result is pass:" << rs.a;
    return 0;
}
