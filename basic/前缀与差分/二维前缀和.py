from typing import List


class PreSum2D:
    """二维前缀和（矩阵不可变）"""
    def __init__(self, matrix: List[List[int]]):
        """初始化二维前缀和数组"""
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i][j - 1] + self.pre_sum[i - 1][j] + \
                                     matrix[i - 1][j - 1] - self.pre_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """计算子矩阵和

        Args:
            row1: 左上角顶点横坐标
            col1: 左上角顶点纵坐标
            row2: 右下角顶点横坐标
            col2: 右下角顶点纵坐标
        
        Returns:
            int: 子矩阵和
        """
        return self.pre_sum[row2 + 1][col2 + 1] - \
               (self.pre_sum[row2 + 1][col1] + self.pre_sum[row1][col2 + 1]) + \
               self.pre_sum[row1][col1]