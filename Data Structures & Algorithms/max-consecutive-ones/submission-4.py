class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0 
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            output = max(output, count)
        return output            