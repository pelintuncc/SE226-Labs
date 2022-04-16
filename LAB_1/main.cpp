#include <iostream>
using namespace std;

int main() {
     string studentName;
     int studentId;

     cout << "What is your name? "<< endl;
     cin >> studentName ;
     cout <<"Hello " + studentName + "!"<< endl;

     cout << "Enter your student ID? "<< endl;
     cin >> studentId ;
     cout <<"Student ID: " + studentId ;


     int number1,number2;
     cout << "You will enter two number and I'll do sum calculations :)" << endl;
     cout <<"Enter the first number: ";
     cin >> number1;
     cout <<"Enter the second number: ";
     cin >> number2;

     int sum = number1 + number2;
     int diff = number1 - number2;
     int mltp = number1 * number2;
     cout << "Summation is: " <<sum << endl;
     cout << "Difference is: " << diff << endl;
     cout << "Multiplication is: "<< mltp << endl;













    return 0;
}
