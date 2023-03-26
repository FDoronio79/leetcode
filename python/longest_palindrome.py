class Solution:
    def longestPalindrome(self, s: str) -> int:
        #create a dictionary to capture the frequency of each letter in the string
        letter_count = {}
        #iterate through the string with each character
        for char in s:
            #check if character is in the dictionary
            if char not in letter_count:
            #if not add the character into the dictionary and set value to 1
                letter_count[char] = 1
            #else increment value of char by 1
            else:
                letter_count[char] += 1

        #create a result variable and set to 0
        result = 0
        #create a odd variable
        odd = 0

        #if the length of the dictionary is equal to 1 return value of key because it will always be a palindrome
        if len(letter_count) == 1:
            return letter_count[s[0]]
        
        #iterate through all of the values
        for val in letter_count.values():
            #check if value is greater than 1
            if val > 1:
                #if value % 2 == 0 (its even) add value to res
                if val % 2 == 0:
                    result += val
                #else
                else:
                    #add value - 1 to the result
                    result += val - 1
                    #add 1 to odd because the value is odd
                    odd += 1
            #else add 1 to odd
            else:
                odd += 1

        #check if the value of odd is greater than 0
        if odd > 0:
            #if it is add 1 to result because we can always add only 1 char into the palindrome from any odd character count
            result += 1
        #return the result
        return result