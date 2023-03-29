class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci sequence/numbers
        p1,p2 = 1,0

        for i in range(n):
            p1,p2 = p1 + p2, p1
        return p1