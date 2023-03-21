from collections import 

class Solution:
    #solution 1
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup_rn = {}
        lookup_mag = {}
        lookup_rn = Counter(ransomNote)
        lookup_mag = Counter(magazine)

        result = lookup_rn - lookup_mag
        if result == {}:
            return True
        return False
    
    #faster solution
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        rn = list(ransomNote)
        mag = list(magazine)

        count = 0
        for c1 in rn:
            for c2 in mag:
                if c1 == c2:
                    mag.remove(c1)
                    count += 1
                    # add break to make it more efficient because once it finds a match it'll break out from the loop and move on to the next iteration
                    break

        return True if count == len(ransomNote) else False