# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/




class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices) == 2:
        #     if prices[1] > prices[0]:
        #         return prices[1]-prices[0]
        if len(prices) < 20:
            max=0;
            for idx in range(len(prices)-1) : 
                l, r = idx, idx+1
                maxYet = 0
                #print("maxYet is " +str(maxYet))

                while r < len(prices):
                    if prices[r] - prices[l] > maxYet:
                        maxYet = prices[r]-prices[l]
                    r+=1

                if(maxYet > max):
                    max = maxYet
 
            return max

        max = 0
        
        diff = dict()
        previous = prices[0]
        newIt = 0;
        downing, upping = False, False
        for idx, dingo in enumerate(prices):
            if newIt == 0:
                diff[newIt] = dingo
                newIt+=1
            elif(dingo > previous and upping != True):
                diff[newIt] = previous
                newIt+=1
                diff[newIt] = dingo;
                
                newIt+=1
                previous = dingo;
                upping, downing = True, False 
            elif(dingo < previous and downing != True):
                
                previous = dingo;
                upping, downing = False, True
            elif idx == len(prices)-1:
                diff[newIt] = dingo
            elif dingo > previous:
                upping, downing = True, False 
            elif dingo < previous:
                upping, downing = False, True 


        print(diff)
        dictLength = len(diff)






        for idx in range(dictLength-1): #going one by one
            l, r = idx, idx+1
            # print(l, r)
            # print(dictLength)
            maxYet = 0
            #print("maxYet is " +str(maxYet))

            while r <dictLength:
                # print(l, r)
                # print(dictLength)
                # print(diff[l], diff[r])
                if diff[r] - diff[l] > maxYet:
                    maxYet = diff[r]-diff[l]
                r+=1

            if(maxYet > max):
                max = maxYet
 
        return max
            
dingo = Solution()
obj = [7, 1, 5, 3, 6, 4]
obj2 = [7,6,5,4,3,2,1]
obj3 = [1,2,3,4,5,6,7]
obj4 = [1,2]
print(dingo.maxProfit( obj))
print(dingo.maxProfit( obj2))
print(dingo.maxProfit( obj3))
print(dingo.maxProfit( obj4))


##failure

# neetcode/GH solution
# 88 rt, 54 mem

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = int
        max_prof = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]- min_price > max_prof:
                max_prof = prices[i] - min_price
            
        return max_prof