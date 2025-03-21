class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=''.join(c.lower for c in s if c.isalpha())
        return s==s[::-1]


solution = Solution()
solution.ispalindrome("racecar")