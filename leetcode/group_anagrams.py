# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Medium

from collections import defaultdict


class Solution:
    # Time Cx: O(n^2), Space Cx: O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_tuple = [tuple(sorted(s)) for s in strs]
        anagram_to_indices: defaultdict[tuple[str, ...], list[int]] = defaultdict(list)
        for index, s in enumerate(strs_tuple):
            ana_indices = anagram_to_indices[s]
            ana_indices.append(index)

        return [
            [strs[index] for index in indices]
            for indices in anagram_to_indices.values()
        ]

    # Time Cx: O(n^2), Space Cx: O(n) for output list
    def groupAnagramsSorting(self, strs: list[str]) -> list[list[str]]:
        res: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            group = res["".join(sorted(s))]
            group.append(s)
        groups = list(res.values())
        return groups

    def groupAnagramsOrd(self, strs: list[str]) -> list[list[str]]:
        res: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord("a")
                count[index] += 1
            group = res[tuple(count)]
            group.append(s)
        return list(res.values())
