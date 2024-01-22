#include <iostream>

using namespace std;
class accessspecifier
{public:

    int a =40;
private:
    int b=23
    int useclass()
    {
        int c;
        c=b;
    }




};

int main()
{
   accessspecifier as;
  cout<< as.a+9;

    return 0;
}
