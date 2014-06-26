def maxProfit(prices):
    if prices == []:
        return 0
        
    lowest = prices[0]    
    max_profit = 0
    for price in prices[1:]:
        if price < lowest:
            lowest = price
            
        max_profit = max(max_profit, price - lowest)
        
    return max_profit
        


print maxProfit([1,2,3,4,5]) # 4
print maxProfit([4,1,2]) # 1
print maxProfit([1,10,2,20]) # 19
print maxProfit([6,1,3,2,4,7]) # 6
