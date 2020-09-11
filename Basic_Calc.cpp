// This is a Basic Calculator built in C++
// Coded by Kyle Spencer

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // Variable Declaration
    int selection = 0;
    float number_1;
    float number_2;
    float result;

    // Main Body of Program
    cout << "Welcome to Basic Calculator: C++!" << endl;
    cout << "This executable was coded by Kyle Spencer!" << endl;

    cout << "What operation would you like to perform?" << endl;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Division" << endl;

    cin >> selection;

    if (selection == 1) {
        cout << "You have selected 1. Addition" << endl;
        cout << "Please enter your first number." << endl;
        cin >> number_1;
        cout << "Please enter your second number." << endl;
        cin >> number_2;
        result = number_1 + number_2;
        cout << "Your result is: " << result << endl;
    } 
    else if (selection == 2) {
        cout << "You have selected 2. Subtraction" << endl;
        cout << "Please enter your first number." << endl;
        cin >> number_1;
        cout << "Please enter your second number." << endl;
        cin >> number_2;
        result = number_1 - number_2;
        cout << "Your result is: " << result << endl;
    } 
    else if (selection == 3) {
        cout << "You have selected 3. Multiplication" << endl;
        cout << "Please enter your first number." << endl;
        cin >> number_1;
        cout << "Please enter your second number." << endl;
        cin >> number_2;
        result = number_1 * number_2;
        cout << "Your result is: " << result << endl;
    } 
    else if (selection == 4) {
        cout << "You have selected 4. Division" << endl;
        cout << "Please enter your first number." << endl;
        cin >> number_1;
        cout << "Please enter your second number." << endl;
        cin >> number_2;
        result = number_1 / number_2;
        cout << "Your result is: " << result << endl;
    }
    else if (selection == 69) {
        cout << "Nice!" << endl;
        system("pause");
        return 0;
    }
    else {
        cout << "You did not select a valid selection." << endl;
        cout << "Why must you try to break my program?" << endl;
        system("pause");
        return 0;
    }

        cout << "Thank you for using Basic_Calc: C++!" << endl;

    system("pause");
    return 0;
}