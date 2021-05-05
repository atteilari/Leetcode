### Author: Atte Tarkiainen ###
### Build Date: 15.4.2021 ###

class DisappearedNumbers:
    def __init__(self, nums):
        self.nums = nums
        self.compare = list(range(1, len(nums) + 1))
        self.solution = []
    
    def main(self):
        for i in self.compare:
            if i not in self.nums:
                self.solution.append(i)

        print(self.solution)

nums = [4,3,2,7,8,2,3,1]
disappearedNumbers = DisappearedNumbers(nums)
disappearedNumbers.main()
