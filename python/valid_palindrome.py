class Solution:
    def isPalindrome1(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

    def alpha_num(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))

    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alpha_num(s[left]):
                left += 1
            while right > left and not self.alpha_num(s[right]):
                right += 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
