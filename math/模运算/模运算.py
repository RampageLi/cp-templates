"""模运算相关

常用恒等式：
1. (a+b) mod m=((a mod m)+(b mod m))mod m
2. (a⋅b) mod m=((a mod m)⋅(b mod m))mod m
3. 同余：(x - y) mod m = 0 
4. 负数取模时，可以加一个m：x mod m + m
"""
from typing import List

# LC contest 404-T3
class Solution:
    """
    找最长子序列，保证奇数项相同且偶数项相同
    方法：子序列只与最后两项有关，f[x][y]表示最后两项为x、y的最长子序列长度
    """
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [x % k for x in nums]
        f = [[0] * k for _ in range(k)]

        for x in nums:
            for y in range(k):
                f[y][x] = max(f[y][x], f[x][y] + 1)
        
        ret = 0
        for i in range(k):
            for j in range(k):
                ret = max(ret, f[i][j])
        return ret