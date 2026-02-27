#https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
import random
class RandomizedSet:

    def __init__(self):
        self.rset=set()

    def insert(self, val: int) -> bool:
        if val not in self.rset:
            self.rset.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        idx= random.randint(0,len(self.rset)-1)
        return list(self.rset)[idx]