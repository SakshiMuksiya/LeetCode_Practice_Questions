#https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

class MinStack:

    def __init__(self):
        self.st=[]
        self.min_st=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val<=self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        if not self.st:
            return
        x = self.st.pop()
        if self.min_st and x== self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
