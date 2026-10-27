class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap_dict = {"}" : "{", "]" : "[", ")" : "("}
        for b in s:
            if b in hashmap_dict:
                if stack and stack[-1] == hashmap_dict[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)      
        return True if not stack else False           
                    
