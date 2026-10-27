class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        score = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1]+stack[-2])
                continue
            if operations[i] == "D":
                stack.append(2*stack[-1])
                continue
            if operations[i] == "C":
               stack.pop()
               continue
            stack.append(int(operations[i]))
        return sum(stack)    



        