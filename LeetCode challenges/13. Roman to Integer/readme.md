### THE PROBLEM

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15 (Constraint 1)
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). (Constraint 2)
It is guaranteed that s is a valid roman numeral in the range [1, 3999]. (Constraint 3)

### THE SOLUTION

First we create a set containing all of the accepted characters that could appear in any given roman numeral, followed by checking if the given input string is a subset of the acccepted character set. (Constraint 2), then we create an if statement to check for the length of the input string (Constraint 1).

When the constraint conditions are met, we create a dictionary with all of the possible roman numerals and their corresponding values (I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900). 

We proceed to iterate over the length of the string. We check if there is more than one letter left in the string. If there is more than one letter in the string, we take a two character slice from the string and check that against the value dictionary. If the two character slice is in the value dictionary, we know it's one of the special cases (IV, IX, XL, XC, CD or CM) and we add the corresponding value to the solution number.

If the two character slice is not in the values dictionary (eg. II or MM) we move on and we add the corresponding value of the single character that we're currently iterating to the solution number.

After the entire length of the string has been iterated over, we return the solution number as the solution. If any of the constraints are not passed, we return an error message about the constraints.


### TO DO
Constraint 3 is largely un implemented