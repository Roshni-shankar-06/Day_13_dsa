class Solution:
  def maxPoints(self, points: list[list[int]]) -> int:
    ans = 0

    def gcd(a: int, b: int) -> int:
      return a if b == 0 else gcd(b, a % b)

  
