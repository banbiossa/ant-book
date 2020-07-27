"""
3.3のsegment tree
"""
import numpy as np

# [a, b) に x を加算する
class SegmentRangeAdder:
    def __init__(self, data_size):
        self.data_range = np.zeros(data_size)
        self.data_point = np.zeros(data_size)

    def add(self, start: int, end: int, x: int, node: int, left: int, right: int):
        """
        [start, end) にxを加算する
         k は接点の番号で、区間[l, r) に対応する
         left, right は常に2の累乗

                        0: [0, 8)
                  1: [0, 4) 2: [4, 8)
         3: [0, 2) ...
        """
        # start <= left <= right <= end
        # 包含
        if start <= left and right <= end:
            self.data_range[node] += x

        # start , left < end , right
        # 入れ子
        # 各 node に x を足す
        # 再起的に子ノードにも x を足す
        elif left < end and start < right:
            self.data_point[node] += (min(end, right) - max(start, left)) * x
            middle = int((left + right) / 2)
            self.add(start, end, x, node * 2 + 1, left, middle)
            self.add(start, end, x, node * 2 + 2, middle, right)

    def sum(self, start: int, end: int, node: int, left: int, right: int):
        """
        [start, end) の和を計算する
        node は接点の番号で、[left, right) に対応する
        """
        # start,end <= left,right or left,right <= start,end
        # 被りがない場合
        if end <= left or right <= start:
            return 0

        # start <= left <= right <= end
        # 包含 (node 0 のみで計算可能)
        elif start <= left and right <= end:
            return self.data_range[node] * (right - left) + self.data_point[node]

        # start , left < end , right
        # 入れ子
        # 各 node に x を足す
        # 再起的に子ノードにも x を足す
        else:
            res = (min(end, right) - max(start, left)) * self.data_range[node]
            middle = int((left + right) / 2)
            res += self.sum(start, end, node * 2 + 1, left, middle)
            res += self.sum(start, end, node * 2 + 2, middle, right)

    def solve(self, A, N, Q, T, L, R, X):
        """
        解く
        Args:
            A: values to add
            N: number of nodes,
            Q: the number of queries
            T: query, C: add, Q: calculate
            L: the left ends
            R: the right ends
            X: the values to add

        """
        # initialize
        for i in range(N):
            self.add(start=i, end=i + 1, x=A[i], node=0, left=0, right=N)

        # solve the queries
        for i in range(Q):
            if T[i] == "C":
                self.add(start=L[i], end=R[i] + 1, x=X[i], node=0, left=0, right=N)
            else:
                print(self.sum(L[i], R[i] + 1, 0, 0, N))
