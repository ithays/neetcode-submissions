class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        score = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                a = stack.pop()
                b = stack.pop()
                s = int(a)+int(b)
                stack.append(b)
                stack.append(a)
                stack.append(s)
                continue
            if operations[i] == "D":
                d = stack[-1]
                stack.append(2*int(d))
                continue
            if operations[i] == "C":
               stack.pop()
               continue
            stack.append(operations[i])
        k=0    
        while k < len(stack):
            sc = stack[k]
            print("k = {}".format(sc))
            score += int(sc)
            k += 1
        return score    



        