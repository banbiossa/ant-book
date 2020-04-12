from typing import List
import numpy as np


class BubbleSortCounter:
    def __init__(self, n: int, array: List):
        """ Make a bubble sort counter from binary indexed tree

        Args:
            n: length of list
            a: list to sort

        Attributes:
            bit: The numbers to keep track of
                The sum of the leaves of [0-a_i]
        """
        self.n = n
        self.array = array
        # [1, n] の数を利用したい
        self.bit = np.zeros(n + 1)

    def add(self, index: int, value: float):
        """Add `value` to bit[`index`] and update the leaves

        Args:
            index(int):
            value(float):
        """
        while index <= self.n:
            self.bit[index] += value
            # get the lowest bit of index, and add
            # this will traverse up the binary tree, 5(0101)-> 6(0110) -> 8(1000)
            index += index & -index

    def reduce_sum(self, index: int):
        """Reduct the tree into one sum
            This will add the sum of bit[0:index]

        Args:
            index(int): last index of the range to sum
        """
        sum_adder = 0
        while index:
            sum_adder += self.bit[index]
            # remove the last bit
            # this will travese the tree downwards, from 5(0101)->4(0100)->0
            index -= index & -index
        return sum_adder

    def solve(self):
        """Solve the bubble sort problem
        """
        ans = 0
        for j in range(self.n):
            ans += j - self.reduce_sum(self.array[j])
            self.add(self.array[j], 1)
        return ans


if __name__ == "__main__":
    n = 4
    a = [3, 1, 4, 2]
    solver = BubbleSortCounter(n, a)
    solver.solve()
