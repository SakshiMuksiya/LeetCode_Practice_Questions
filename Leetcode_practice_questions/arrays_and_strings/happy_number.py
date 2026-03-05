#https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

#solution
def isHappy(self, n: int) -> bool:
        if (n==1 or n==7):
            return True
        elif (n<10):
            return False
        else:
            sum=0
            while(n>0):
                temp=n%10
                sum+=temp*temp
                n=n//10
            return self.isHappy(sum)