class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sm = Counter(s)
        st = Counter(t)
        return sm == st