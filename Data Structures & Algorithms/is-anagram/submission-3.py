class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ar = [0] * 26
        for i in s:
            ar[ord(i) - ord('a')] += 1

        for i in t:
            ar[ord(i) - ord('a')] -= 1

        for a in ar:
            if a != 0:
                return False
        return True