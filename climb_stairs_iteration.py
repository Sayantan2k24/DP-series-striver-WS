# from leetcode --> https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):

        if n <=1: 
            return 1
        
        prev = 1 # at 0 stair
        prev2 = 1 # at stair 1

        # from 2 to n --> inlcude n
        for i in range(2,n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi

        return curi
    

n = int(input("Enter the final stair number to go: "))
sol = Solution()

print(sol.climbStairs(n))
