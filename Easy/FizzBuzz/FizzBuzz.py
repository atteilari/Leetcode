### Author: Atte Tarkiainen ###
### Build Date: 15.4.2021 ###

class FizzBuzz:
    def __init__(self, n):
        self.list = list(range(1, n + 1))
        self.solution = []
    
    def main(self):
        for i in self.list:
            if i % 15 == 0:
                self.solution.append("FizzBuzz")
            elif i % 3 == 0:
                self.solution.append("Fizz")
            elif i % 5 == 0:
                self.solution.append("Buzz")
            else:
                self.solution.append(i)
        print(self.solution)

n = 100
fizzBuzz = FizzBuzz(int(n))
fizzBuzz.main()
