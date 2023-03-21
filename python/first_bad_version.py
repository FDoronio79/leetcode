# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    #naive solution, issue is timeout with larger n value
    def firstBadVersion(self, n: int) -> int:
        for i in range(n + 1):
            if isBadVersion(i):
                return i
            
    #other solution
    def firstBadVersion(self, n:int) -> int:
        l = 1
        h = n
        result = n
        
        while l <= h:
            m = (l + h) // 2
            if isBadVersion(m):
                result = m
                h = m - 1
            else:
                l = m + 1
        return result
    