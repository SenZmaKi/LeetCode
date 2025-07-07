# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Medium


# Time Cx: O(n), Space Cx: O(n)
class Node:
    def __init__(
        self,
    ) -> None:
        self.is_terminal = False
        self.children: dict[str, "Node"] = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            node = curr.children.get(char)
            if node is None:
                node = Node()
                curr.children[char] = node
            curr = node
        curr.is_terminal = True

    def find_final_node(self, word: str) -> Node | None:
        curr = self.root
        for char in word:
            node = curr.children.get(char)
            if node is None:
                return None
            curr = node
        return curr

    def search(self, word: str) -> bool:
        node = self.find_final_node(word)
        return node is not None and node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.find_final_node(prefix)
        return node is not None


# Time Cx: O(n), Space Cx: O(n)
class NodeArray:
    def __init__(
        self,
    ) -> None:
        self.is_terminal = False
        self.children: list["NodeArray | None"] = [None] * 26

    def find_child(self, char: str) -> "NodeArray | None":
        index = NodeArray.find_child_index(char)
        return self.children[index]

    @staticmethod
    def find_child_index(char: str) -> int:
        index = ord(char) - ord("a")
        return index


class TrieArray:
    def __init__(self):
        self.root = NodeArray()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = NodeArray.find_child_index(char)
            node = curr.children[index]
            if node is None:
                node = NodeArray()
                curr.children[index] = node
            curr = node
        curr.is_terminal = True

    def find_final_node(self, word: str) -> NodeArray | None:
        curr = self.root
        for char in word:
            node = curr.find_child(char)
            if node is None:
                return None
            curr = node
        return curr

    def search(self, word: str) -> bool:
        node = self.find_final_node(word)
        return node is not None and node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.find_final_node(prefix)
        return node is not None
