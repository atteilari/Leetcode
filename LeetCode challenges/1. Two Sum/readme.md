### THE PROBLEM

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104 (constraint 1)
-109 <= nums[i] <= 109 (constraint 2)
-109 <= target <= 109 (constraint 3)
Only one valid answer exists. (constraint 4)


### THE SOLUTION

First we constrain the for loop's action behind two nested if statements (constraints 1 & 2). If the input is within the constraints, we create an empty list item to store our solution in the future.

Starting from the first item in the input list we iterate over the entire list. The only exception being the very last item in the list, since we know that if we have reached the final item in the list at this point, there is no possible solution.

During every iteration we create a complementary number for the item we're currently iterating over. The idea is that the values of the item we're currently iterating and it's complementary number must equal to our target. (number + complementary number == target)

After creating the complementary number we look for said complementary number in the list using an if statement. If the complementary number appears in the list we know that the target can be reached (because number + complementary = target). We append both the index of the item we're iterating over + the index of our complementary number to the solution list we created at the start.

Finally we check the length of the solution list. If the length is == 1, we can return the indices as there is only a singular correct answer. If the length is > 1 we know there are multiple solutions and as per constraint 4 we return an error message. Finally if the length of the list is neither of the beforementioned, we know that there is no solution to the input.