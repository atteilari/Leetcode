class Solution(object):
    def longestCommonPrefix(strs):
        if len(strs) < 1 or len(strs) > 200: # Constraint 1
            return "Input contains too many or not enough strings (Constraint 1)"
        
        for i in strs: # Constraint 2
            if len(i) < 0 or len(i) > 200:
                return "Input contains a string that is too long or too short (Constraint 2)"
        
        accepted = set("abcdefghijklmnopqrstuvwxyz") # Constraint 3
        for i in strs:
            if not set(i).issubset(accepted):
                return "Input contains unallowed characters (Constraint 3)"
        
        return "Constraints passed"
                
    
# Example inputs
solution = Solution.longestCommonPrefix(["flower","flow","flight"])
print(solution)
solution = Solution.longestCommonPrefix(["dog","racecar","car"])
print(solution)

# Example inputs for constraints
solution = Solution.longestCommonPrefix([]) # Constraint 1
print(solution)
solution = Solution.longestCommonPrefix(["a" * 250, "b" * 10]) # Constraint 2
print(solution)
solution = Solution.longestCommonPrefix(['Äiti', "racecar", "car"]) # Constraint 3
print(solution)