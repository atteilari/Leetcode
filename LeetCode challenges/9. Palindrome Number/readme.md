### The Problem

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1 (Constraint 1)

### The solution

First implement the constraint via if statement. After the if statement, convert the int input into a str. Slice the str in reverse and store it in a new variable. Finally check if both strings are an exact match. If yes, return True, if not return False.