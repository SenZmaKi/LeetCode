# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/description/

# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/description/


class MyHashMap:
    def __init__(self):
        self.array: list[int | None] = []

    def _is_valid_index(self, index: int) -> bool:
        return len(self.array) > index

    def put(self, key: int, value: int) -> None:
        if not self._is_valid_index(key):
            self.array.extend([None] * (key + 1))
        self.array[key] = value

    def get(self, key: int) -> int:
        value = self.array[key] if self._is_valid_index(key) else None
        if value is None:
            return -1
        return value

    def remove(self, key: int) -> None:
        value = self.get(key)
        if value != -1:
            self.array[key] = None


class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMapCorrect:
    def __init__(self):
        self.map = []

        for _ in range(1000):
            self.map.append(Node())

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return

            cur = cur.next

        cur.next = Node(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

    def hash(self, key):
        return key % len(self.map)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
k = 1
v = 69
obj.put(k, v)
param_2 = obj.get(k)
obj.remove(k)
