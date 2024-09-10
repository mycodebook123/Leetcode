import math
class Solution:
    def smallestEvenMultiple(self, n):
        a = 2
        b = n
        
        gcd = math.gcd(a, b)
        
        lcm = abs(a*b)//gcd
        
        return lcm
solution_instance = Solution()
    
print (solution_instance.smallestEvenMultiple(5))
    