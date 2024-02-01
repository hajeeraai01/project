#include <iostream>

using namespace std;

int main()
 {

    /*string name;
    cout<< "enter your name :" << endl;
    cin >> name;
    cout <<name <<endl;
    fflush(stdin);
    cout <<"enter your name :"<< endl;
    getline(cin,name);
    cout << name << endl;*/


    int main();
    string firstname;
    cin>>firstname;
    string lastname;
    cin>>lastname;

    cout << firstname +" "+ lastname ;
    string fullname = firstname.append(lastname);
    cout<<fullname<<endl;

    lastname.push_back('z');
    cout<<lastname<<endl;


   firstname.push_back('mr');
   cout<<firstname;
   cout<<firstname;

   cout<<fullname.length();
   cout<<fullname.size();


    return 0;
}







