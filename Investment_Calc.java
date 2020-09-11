// This is an Investment Calculator built in Java
// Coded by Kyle Spencer

import java.util.Scanner;

public class Investment_Calc {
    public static void main(String[] args) {
        // Variable Declaration
        int years;
        float current_principal;
        float monthly_invest;
        float yearly_invest;
        float interest_rate;
        float final_total = 0;
        Scanner input = new Scanner(System.in);

        // Main Program Body
        System.out.println("Welcome to Investment Calculator: Java!");
        System.out.println("\n");

        System.out.println("Please enter your starting principal: ");
        String principal = input.next();
        current_principal = Float.parseFloat(principal);

        System.out.println("Please enter how much you invest each month: ");
        String amount = input.next();
        monthly_invest = Float.parseFloat(amount);
        yearly_invest = monthly_invest * 12;

        System.out.println("How many years are you planning to invest?: ");
        String time = input.next();
        years = Integer.parseInt(time);

        System.out.println("What do you estimate will be the yearly interest of your investments? (10% = 0.1)");
        String interest = input.next();
        interest_rate = Float.parseFloat(interest);

        System.out.println("\n");

        if (current_principal == 0) {
            final_total = final_total + 0;
        } else {
            final_total = final_total + current_principal;
        }

        for (int i = 1; i <= years; i++) {
            final_total = (final_total + yearly_invest) * (1 + interest_rate);
        }

        final_total = Math.round(final_total);
        String final_string = String.format("%.10f", final_total);

        System.out.println("Your total is: " + final_string);
        System.out.println("Thank you for using Investment Calculator: Java!");

        input.close();
    }
}