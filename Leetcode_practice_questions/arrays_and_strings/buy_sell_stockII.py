#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def maxProfit(prices) :
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                profit+= (prices[i]-prices[i-1])
        return profit