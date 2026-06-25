class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_counter = {}
        for x in s:
            s_counter[x] = s_counter.get(x, 0) + 1

        t_counter = {}
        for x in t:
            t_counter[x] = t_counter.get(x, 0) + 1
        return s_counter == t_counter