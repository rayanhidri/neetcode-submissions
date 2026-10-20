class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_index = 0        # jour d’achat optimal (jusqu’ici)
        max_profit = 0

        for i in range(1, n):   # on commence à 1 car on compare avec min_index
            if prices[i] < prices[min_index]:
                # si on trouve un prix plus bas, c’est un meilleur jour d’achat
                min_index = i
            else:
                # calculer le profit si on vend aujourd’hui
                profit = prices[i] - prices[min_index]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

            

        

        