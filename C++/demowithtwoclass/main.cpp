#include <iostream>

using namespace std;
class problems

{
    public:

    problems()
    {
        int x, y, z;
        cin>>x>>y>>z;
        cout<<"check files and operator"<<(x>y)&&(y>z);

    }
     problems(int x,int y, int z)
     {
        cout<<"check files and operator"<<(x>y)&&(x>z);
     }


};

class usingfunction
{
public:

        void dividevalue()
        {
            int totalvalue;
            cin >>totalvalue;
            totalvalue /=20;
            cout <<"divide equal is \n"<<totalvalue;
        }
        void concadenation()
        {
            string a,b,c;
            cin >>a>>b>>c;
            cout <<"concadenation is\n"<<(a+b+c);
        }
        void concadenation(string name1,string name2)
        {

            cout <<"concatenate two string\n"<<(name1+name2);

        }
};

int main()

{
    problems pb;
    problems pb1 (66,55,44);
    usingfunction uf,uf1,uf2;
    uf.dividevalue();
    uf1.concadenation();
    uf2.concadenation("mahreen","rafan");
     return 0;
}
