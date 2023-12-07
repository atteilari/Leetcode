class Solution(object):
    def isValid(s):
        if len(s) < 1 or len(s) > pow(10, 4): # Constraint 1
            return "Invalid input, the string is too short or long (Constraint 1)"
        
        accepted = set("()[]{}") # Constraint 2
        if not set(s).issubset(accepted): # Constraint 2
            return "Invalid input, the string contains characters that are not accepted (Constraint 2)"
        
        return "Constraints passed"

        

# Example inputs
solution = Solution.isValid("()")
print(solution)
solution = Solution.isValid("()[]{}")
print(solution)
solution = Solution.isValid("(]")
print(solution)

"""
# Example inputs for constraints
solution = Solution.isValid("") # Constraint 1
print(solution)
solution = Solution.isValid("(ABC)")
print(solution)
"""