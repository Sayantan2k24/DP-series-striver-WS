# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

# i i-1 i-2

# left = f(i-1) + delta
# right = f(i-2) + delta

# right only works -- when i > 1

# recursion

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
📊 Let's Check the Correct Answer:
For heights = [2, 1, 3, 5, 4], and n = 4 (destination: stair index 4):

All possible valid paths:

0→1→2→3→4 = |2-1| + |1-3| + |3-5| + |5-4| = 1+2+2+1 = 6

0→2→3→4 = |2-3| + |3-5| + |5-4| = 1+2+1 = 4

0→1→3→4 = |2-1| + |1-5| + |5-4| = 1+4+1 = 6

0→2→4 = |2-3| + |3-4| = 1+1 = 2 ✅ Minimum

0→1→2→4 = |2-1| + |1-3| + |3-4| = 1+2+1 = 4

So, the correct answer is 2, but your code returns 3.
'''


