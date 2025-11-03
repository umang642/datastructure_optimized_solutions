from typing import List

class BestTimeToBuy:
    def get_the_max_profit(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_profit:
                min_profit = price 
            
            profit = price - min_profit

            if max_profit < profit:
                max_profit = profit

        return max_profit

if __name__ == "__main__":
    prices = [7,1,2,3,45,6]
    s = BestTimeToBuy()
    print(s.get_the_max_profit(prices=prices))
    