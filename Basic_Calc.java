// This is a Basic Calculator built in Java
// Coded by Kyle Spencer

import java.util.Scanner;

public class Basic_Calc {
    public static void main(String[] args) {
        // Variable Declaration
        int selection_int;
        float first_number;
        float second_number;
        float result;
        Scanner input = new Scanner(System.in);

        // Main Program Body
        System.out.println("Welcome to Basic Calculator: Java!");
        System.out.println("\n");
        
        System.out.println("Here are your options:");
        System.out.println("1: Addition");
        System.out.println("2: Subtraction");
        System.out.println("3: Multiplication");
        System.out.println("4: Division");
        System.out.println("\n");

        System.out.println("What is your selection?");
        String selection = input.next();
        selection_int = Integer.parseInt(selection);

        if (selection_int == 1) {
            System.out.println("You have chosen Addition!");
            System.out.println("Please enter your first number.");
            String number_one = input.next();
            first_number = Float.parseFloat(number_one);

            System.out.println("Please enter your second number.");
            String number_two = input.next();
            second_number = Float.parseFloat(number_two);

            result = first_number + second_number;
            System.out.println(result);
        }
        else if (selection_int == 2) {
            System.out.println("You have chosen Subtraction!");
            System.out.println("Please enter your first number.");
            String number_one = input.next();
            first_number = Float.parseFloat(number_one);

            System.out.println("Please enter your second number.");
            String number_two = input.next();
            second_number = Float.parseFloat(number_two);

            result = first_number - second_number;
            System.out.println(result);
        }
        else if (selection_int == 3) {
            System.out.println("You have chosen Multiplication!");
            System.out.println("Please enter your first number.");
            String number_one = input.next();
            first_number = Float.parseFloat(number_one);

            System.out.println("Please enter your second number.");
            String number_two = input.next();
            second_number = Float.parseFloat(number_two);

            result = first_number * second_number;
            System.out.println(result);
        }
        else if (selection_int == 4) {
            System.out.println("You have chosen Division!");
            System.out.println("Please enter your first number.");
            String number_one = input.next();
            first_number = Float.parseFloat(number_one);

            System.out.println("Please enter your second number.");
            String number_two = input.next();
            second_number = Float.parseFloat(number_two);

            result = first_number / second_number;
            System.out.println(result);
        }
        else if (selection_int == 69) {
            System.out.println("Nice!");
        }
        else {
            System.out.println("You have entered an invalid selection.");
            System.out.println("Thank you for using Basic_Calc: Java");
        }

        input.close();
    }
}