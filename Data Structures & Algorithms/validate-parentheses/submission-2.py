class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False  
        stack.append(s[0])    
        for i in range(1,len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if stack[-1] == "{" and s[i] == "}":
                stack.pop()
            elif stack[-1] == "[" and s[i] == "]":
                stack.pop() 
            elif stack[-1] == "(" and s[i] == ")":
                stack.pop() 
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True    

        