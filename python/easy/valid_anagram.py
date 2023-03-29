class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))

        return s1 == t1
    
    #hash map solution

    def isAnagramhas(self, s:str, t:str) -> bool:
        if len(t) != len(s):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            #the get method allows for an optional return value if the key does not exist
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t