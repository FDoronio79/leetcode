class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')':'(', ']': '[', '}': '{'}

        for p in s:
            if p in lookup.values():
                stack.append(p)
            elif stack and lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
    
    #other solution
    def isValid2(self, s: str) -> bool:
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return False if len(s) != 0 else True