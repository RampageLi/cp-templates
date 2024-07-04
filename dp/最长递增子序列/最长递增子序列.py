"""
采用 二分+贪心 确定每个元素在答案数组中的位置

常用技巧：
1. 前后缀分解：统计以每个元素为结尾，从左、从右最长递增序列

题目：
1671. 得到山形数组的最少删除次数
"""
from bisect import bisect_right, bisect_left
from typing import List


def LIS1(nums: List[int]) -> int:
    """
    非严格递增
    """
    n = len(nums)
    ans = [nums[0]]

    for i in range(1, n):
        if nums[i] >= ans[-1]:
            ans.append(nums[i])
        else:
            idx = bisect_right(ans, nums[i])
            ans[idx] = nums[i]

    return len(ans)

def LIS2(nums: List[int]) -> int:
    """
    严格递增
    """
    n = len(nums)
    ans = [nums[0]]

    for i in range(1, n):
        idx = bisect_left(ans, nums[i])
        if idx == len(ans):
            ans.append(nums[i])
        else:
            ans[idx] = nums[i]
    return len(ans)


if __name__ == "__main__":
    arr = [1, 1, 2]
    print("数组：", arr)
    print("非严格递增最长子序列长度：", LIS1(arr))
    print("严格递增最长子序列长度：", LIS2(arr))