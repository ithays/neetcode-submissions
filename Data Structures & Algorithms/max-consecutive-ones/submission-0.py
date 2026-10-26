class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                if res < count:
                    res = count
                count = 0
        if res < count:
            res = count        
        return res
                
        