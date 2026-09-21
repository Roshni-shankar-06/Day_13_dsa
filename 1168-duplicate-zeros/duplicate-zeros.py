class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = arr.count(0)
        i = len(arr) - 1
        j = len(arr) + zeros - 1
        
      
