from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to infinity so the first price becomes the minimum
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # If we find a new lowest price, we "buy" (virtually) on this day
            if price < min_price:
                min_price = price
            
            # If the current price is not lower, we check if selling today 
            # yields a better profit than what we have seen before
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

# --- Testing the solution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1: {sol.maxProfit([7,1,5,3,6,4])}") 
    # Expected: 5 (Buy at 1, Sell at 6)

    # Example 2
    print(f"Example 2: {sol.maxProfit([7,6,4,3,1])}")   
    # Expected: 0 (Price only goes down)


"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""
