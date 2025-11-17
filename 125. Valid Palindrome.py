class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_phrase = ""
        for c in s.lower():
            if c.isalnum():
                clean_phrase += c

        left = 0
        right = len(clean_phrase) - 1

        while left < right:
            if clean_phrase[left] != clean_phrase[right]:
                return False
            left += 1
            right -= 1
        
        return True
