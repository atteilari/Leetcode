/* Author: Atte Tarkiainen */
/* Build Date: 15.4.2021 */

package Easy.FizzBuzz;

import java.util.Scanner;
import java.util.ArrayList;

public class FizzBuzz {
    public static void main(String[] args) {
        ArrayList<String> listPrint = new ArrayList<String>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please input a number: ");
        int length = Integer.valueOf(scanner.nextLine());

        for (int i = 1; i <= length; i++) {
            if (i % 15 == 0) {
                listPrint.add("FizzBuzz");
            }
            else if (i % 3 == 0) {
                listPrint.add("Fizz");
            }
            else if (i % 5 == 0) {
                listPrint.add("Buzz");
            }
            else {
                listPrint.add(String.valueOf(i));
            }
        }
        scanner.close();
        System.out.println(listPrint);
    }
}
