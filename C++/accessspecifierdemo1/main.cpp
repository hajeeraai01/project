#include <iostream>
using namespace std;
class salaryprint{

private:
    int salary;

public:
    string empname;

    void setsalary(int s){
    salary =s;
}
int getsalary(){
 return salary;

 }

};


int main(){
salaryprint sp;
sp.setsalary(30);
sp.getsalary();

return 0;

}













/*#include <iostream>

using namespace std;
class accessspecifier{


private:
    int b=25;

protected:
    int pc=90;

public:

    int a,c;
    void printb(){
    c=b;
    cout <<c;
    c=pc;
    cout<<c;

    }

};



int main()
{
   accessspecifier as;
   as.a=30;
   cout<< as.a;
   as.printb();




    return 0;
}
*/




