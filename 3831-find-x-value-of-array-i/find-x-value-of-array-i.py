class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        # dp[r] := number of subarrays ending at the current position with product % k == r
        dp = [0] * k
        
        for num in nums:
            newDp = [0] * k
            numMod = num % k
            
            # Start a new subarray consisting only of the current 'num'
            newDp[numMod] = 1
            
            # Extend all previous subarrays ending at the prior element
            for i in range(k):
                if dp[i] > 0:
                    newMod = (i * numMod) % k
                    newDp[newMod] += dp[i]
            
            # Accumulate the counts of all valid subarrays ending here into our answer
            for i in range(k):
                ans[i] += newDp[i]
                
            dp = newDp
            
        return ans
