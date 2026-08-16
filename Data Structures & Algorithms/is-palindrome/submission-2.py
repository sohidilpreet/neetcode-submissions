class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        half = len(s)//2
        first = s[:half]
        last = s[half+1:len(s)] if len(s)%2!=0 else s[half:len(s)]
        return first.lower() == last[::-1].lower()
