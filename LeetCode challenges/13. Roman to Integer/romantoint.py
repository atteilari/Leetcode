class Solution(object):
    def romanToInt(s):
        if len(s) < 1 or len(s) > 15: # Constraint 1
            return "Input string is too long (Constraint 1)"
        
        accepted = set("IVXLCDM") # Constraint 2
        if not set(s).issubset(accepted): # Constraint 2
            return "Input strings contains characters that are not allowed (Constraint 2)"
        
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} # Create a roman numeral value dictionary
        i = 0
        number = 0
        while i < len(s): # Iterate over the strings length
            if i+1<len(s) and s[i:i+2] in values: # If there is more than 1 letter left in the string and if a 2 character slice of the string appears in the values dictionary
                number+=values[s[i:i+2]] # Add the number corresponding to the value dictionary to the solution
                i+=2
            else: # If there is only a single letter in the string left or if the 2 character slice does not appear in the values dictionary
                number+=values[s[i]] # Add the number corresponding to the value dictionary to the solution
                i+=1
        return number

# Example inputs
solution = Solution.romanToInt("III")
print(solution)
solution = Solution.romanToInt("LVIII")
print(solution)
solution = Solution.romanToInt("MCMXCIV")
print(solution)

"""
# Example inputs for constraints
solution = Solution.romanToInt("MMMMMMMMMMMMMMMMCIV") # Constraint 1
print(solution)
solution = Solution.romanToInt("MCM1") # Constraint 2
print(solution)
"""