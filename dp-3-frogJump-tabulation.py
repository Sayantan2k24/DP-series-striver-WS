# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.
# Memoization --> Tabulation

class Solution:
    def frogJump(self,ind, heights, dp):


        dp[0] = 0 # we know already # for 0 we already know the value -- so can calculate from 1 to n-1, include n-1
        # why N-1 --> given in question --> "climb from the 0th stair to the (N-1)th stair"


        for i in range(1,ind + 1): # whatver part were doing something on ind repeatedly --> make that to i na inlcude in for loop
            fs = dp[i - 1] + abs(heights[i] - heights[i-1])

            ss = float('inf')  # Initialize with infinity # ss is always defined before using it in min(). even when ind ==1 or less than 1
            if i > 1:
                ss = dp[i - 2]+ abs(heights[i] - heights[i-2])
        
            dp[i] = min(fs,ss)

        return dp[n-1] # by the time loop exits -> when i = n, final value already stored in n-1 index



n = int(input("Enter the destination stair number: "))
heights = [2, 1, 3, 5, 4]

# define a dp array globally with size n+1 --> 0 Based index
dp = [-1] * (n+1)

sol = Solution()
print(sol.frogJump(n, heights, dp))



'''
# memoization
class Solution:
    def frogJump(self,ind, heights, dp):

        if ind == 0:
            dp[ind] = 0
            return 0
        
        if dp[ind] != -1:
            return dp[ind]

        fs = self.frogJump(ind - 1, heights,dp) + abs(heights[ind] - heights[ind-1])

        ss = float('inf')  # Initialize with infinity # ss is always defined before using it in min(). even when ind ==1 or less than 1
        if ind > 1:
            ss = self.frogJump(ind -2, heights, dp) + abs(heights[ind] - heights[ind-2])
    
        dp[ind] = min(fs,ss)

        return dp[ind]



n = int(input("Enter the destination stair number: "))
heights = [2, 1, 3, 5, 4]

# define a dp array globally with size n+1 --> 0 Based index
dp = [-1] * (n+1)


sol = Solution()
print(sol.frogJump(n, heights, dp))


'''