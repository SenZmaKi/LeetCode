# 3170. Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description
from typing import NamedTuple
import heapq


class CharAndRevIndex(NamedTuple):
    char: str
    rev_index: int


class Solution:
    def clearStars(self, s: str) -> str:
        seen_heap: list[CharAndRevIndex] = []
        keep_list = [True] * len(s)
        for index, char in enumerate(s):
            if char != "*":
                rev_index = len(s) - index
                c = CharAndRevIndex(char, rev_index)
                heapq.heappush(seen_heap, c)
                continue

            keep_list[index] = False
            if seen_heap:
                smallest = heapq.heappop(seen_heap)
                remove_index = len(s) - smallest.rev_index
                keep_list[remove_index] = False
        clean_s = "".join(char for index, char in enumerate(s) if keep_list[index])
        return clean_s


def main():
    sol = Solution()
    s = "aaba*"
    clean_s = sol.clearStars(s)
    print(f'input: "{s}"')
    print(f'output: "{clean_s}"')


main()
