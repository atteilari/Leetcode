class Solution(object):
    def twoSum(nums, target):
        if len(nums) < 2 or len(nums) > pow(10, 4):  # Constraint 1
            return "The list input is too long or too short (Constraint 1)"
        
        for i in nums: # Constraint 2
            if i < pow(-10, 9) or i > pow(10, 9):  # Constraint 2
                return "List input contains a number too big or too small(Constraint 2)"
        
        if target < pow(-10, 9) or target > pow(10, 9):  # Constraint 3
            return "The target is too big or too small (Constraint 3)"
        
        found_indices = [] # Create a list item to store the solution
        for i, number in enumerate(nums[:-1]):  # Iterate over every item, except the final one
            complementary = target - number  # Calculate the complementary number for the item being iterated
            if complementary in nums[i + 1:]:  # Iterate over the list to find out if the complementary number also appears in the input list
                complement_index = nums.index(complementary, i+1)  # Find the index of the complementary number
                found_indices.append((i, complement_index)) # Add the indices to the 

        if len(found_indices) == 1: # Constraint 4
            return list(found_indices[0])  
        elif len(found_indices) > 1: # Constraint 4
            return "Invalid solution, there are multiple solutions (Constraint 4)"
        else:
            return "No solution found"

# Example inputs
solution = Solution.twoSum([2, 7, 11, 15], 9)
print(solution)
solution = Solution.twoSum([3, 2, 4], 6)
print(solution)
solution = Solution.twoSum([3, 3], 6)
print(solution)

"""
# Example inputs for constraints
solution = Solution.twoSum([1], 6) # Constraint 1
print(solution)
solution = Solution.twoSum([3 * pow(10, 9), 3, 4], 7) # Constraint 2
print(solution)
solution = Solution.twoSum([3, 6, 3, 6, 3, 6], 3 * pow(10, 9)) # Constraint 3
print(solution)
solution = Solution.twoSum([3, 6, 3, 6, 3, 6], 6) # Constraint 4
print(solution)
"""