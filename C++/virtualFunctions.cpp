#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <numeric>
class Person{
    public:
        static int professorCounter;
        static int studentCounter;
        string name;
        int age;
        virtual void getdata() = 0;
        virtual void putdata() = 0;
};
int Person::professorCounter = 0;
int Person::studentCounter = 0;

class Professor : public Person {
    public:
    int cur_id;
        Professor(){
            cur_id = ++professorCounter;
        }
        int publications;
        void getdata() override{
            cin >> name;
            cin >> age;
            cin >> publications;
        };
        void putdata() override{
            cout << name << " ";
            cout << age << " ";
            cout << publications << " ";
            cout << cur_id << endl;
        };
};
class Student : public Person {
    public:
        int cur_id;
        Student(){
            cur_id = ++studentCounter;
        }
        vector<int> marks;
        int mark;
        void getdata() override{
            cin >> name;
            cin >> age;
            for(int i=0; i<6; i++){
                cin >> mark;
                marks.push_back(mark);
            };
        };
        void putdata() override{
            cout << name << " ";
            cout << age << " ";
            cout << accumulate(marks.begin(),marks.end(), 0) << " ";
            cout << cur_id << endl;
        }
};
int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
