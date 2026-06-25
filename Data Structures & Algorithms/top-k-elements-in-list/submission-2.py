class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = [0]*k
        for item in nums:
            d[item]+=1
        
        bucket = [[] for i in range(len(nums)+1)]

        for key, value in d.items():
            bucket[value].append(key)
        l = 0
        for i in range(len(bucket)-1,0 ,-1):
            if not bucket[i]: 
                continue
            for j in bucket[i]:
                ans[l] =j
                l+=1
                if l >=k:
                    return ans
