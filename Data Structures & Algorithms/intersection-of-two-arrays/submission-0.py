class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        seen = set(nums1)
        for n in nums2:
            if n in seen:
                output.append(n)
                seen.remove(n)
        return output        