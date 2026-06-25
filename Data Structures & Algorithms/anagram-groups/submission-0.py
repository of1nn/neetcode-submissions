class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = dict()

        for item in strs:
            char_count = [0]*26
            for ch in item:
                char_count[ord(ch)-ord('a')]+=1
            char_count=tuple(char_count)
            if char_count in m:
                m[char_count].append(item)
            else:
                m[char_count] = [item]
        return list(m.values())