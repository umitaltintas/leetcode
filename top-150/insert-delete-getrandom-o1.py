import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        index = self.index_map[val]
        last = self.nums[-1]
        self.nums[index] = last
        self.index_map[last] = index
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

def test_randomized_set():
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) == True
    assert randomized_set.remove(2) == False
    assert randomized_set.insert(2) == True
    assert randomized_set.getRandom() in [1, 2]
    assert randomized_set.remove(1) == True
    assert randomized_set.insert(2) == False
    assert randomized_set.getRandom() == 2

if __name__ == '__main__':
    test_randomized_set()