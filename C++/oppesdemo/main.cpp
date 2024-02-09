

#include <iostream>

using namespace std;

namespace cat{

    string name= "sweety";
    }

    namespace cat1{
    string name ="sweety";}

    using namespace cat;

  int main()
{
    //string name="sweety";
    cout <<name << endl;

    //string name="sweety";
    cout <<name <<endl;
    cout<< cat1::name<<endl;







    return 0;
}




