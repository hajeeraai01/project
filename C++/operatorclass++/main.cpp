#include <iostream>

using namespace std;

class myfirstclass

{

    public:
    int a=5;
void multiply()
{
    int x,y;
    cin>>x>>y;
    cout<<(x*y);

}
int subtract()
{
    int p,q,r;
    cin>>p>>q;
    r=p-q;
    cout<<r;
}

};
  int addition()
  {   int a,b,c;
      cin>>a>>b;
      c=a+b;
      cout<<c;
  }

int main()
{
    myfirstclass mfc;
    cout << mfc.a;
    mfc.multiply();
    addition();
    mfc.subtract();
    return 0;
}
