class Solution(object):
    def isPalindrome(x):
        if x < -231 or x > 231: # Constraint 1
            return "Invalid input (Constraint 1)"
        
        x = str(x) # Convert int into str
        reverse = x[::-1] # Slice the str in reverse
        if x == reverse: # Check if both strings match
            return True
        else:
            return False

# Example inputs
solution = Solution.isPalindrome(121)
print(solution)
solution = Solution.isPalindrome(-121)
print(solution)
solution = Solution.isPalindrome(10)
print(solution)

"""
# Example inputs for constraints
solution = Solution.isPalindrome(-232)
print(solution)
"""
