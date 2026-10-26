class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        j = 0
        for i in range(len(arr)):
            j = i+1
            if j < len(arr):
                arr[i] = 0
                for k in range(j, len(arr)):
                    arr[i] = max(arr[i], arr[k])
            else:
                arr[i] = -1
        return  arr        
        