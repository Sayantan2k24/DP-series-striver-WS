# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

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



# Recursion
'''
class Solution:
    def frogJump(self,ind, heights):

        if ind == 0:
            return 0
        

        fs = self.frogJump(ind - 1, heights) + abs(heights[ind] - heights[ind-1])

        ss = float('inf')  # Initialize with infinity # ss is always defined before using it in min(). even when ind ==1 or less than 1
        if ind > 1:
            ss = self.frogJump(ind-2, heights) + abs(heights[ind] - heights[ind-2])
    
        return min(fs,ss)



n = int(input("Enter the destination stair number: "))
heights = [2, 1, 3, 5, 4]
sol = Solution()
print(sol.frogJump(n, heights))


'''
