from typing import List

class StockBuyAndSellGetMaxProfit:
    def get_max_profit(self, nums: List[int]) -> int: 

        low = nums[0]
        high = nums[0]
        profit = 0
        i = 0

        while i < len(nums) - 1:

            # get the low price 
            while i < len(nums) - 1 and nums[i] >= nums[i + 1]:
                i += 1
            low = nums[i] 

            # get the high price 
            while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
                i += 1
            high = nums[i]

            # calculate the profit 
            profit += high - low

        # return the profit
        return profit

if __name__ == '__main__':
    nums = [7,1,8,5,4,6,7,8]
    s = StockBuyAndSellGetMaxProfit()
    print(s.get_max_profit(nums = nums))