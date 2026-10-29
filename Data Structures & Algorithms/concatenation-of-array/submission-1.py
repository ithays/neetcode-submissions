class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lnums = len(nums)
        for i in range(lnums):
            nums.append(nums[i])
        return nums    
