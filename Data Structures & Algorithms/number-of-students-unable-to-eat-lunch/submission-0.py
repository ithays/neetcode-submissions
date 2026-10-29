class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        slen = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                slen -=1
                cnt[s] -= 1
            else: 
                return slen    
        return slen        
        