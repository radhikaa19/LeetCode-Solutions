class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for customer in accounts:
            wealth = sum(customer)   # ek customer ke saare banks ka sum
            
            if wealth > max_wealth:
                max_wealth = wealth
                
        return max_wealth
        