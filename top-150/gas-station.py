class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        total_cost = 0
        start = 0
        tank = 0
        
        for i, g in enumerate(gas):
            tank += g - cost[i]
            total_gas += g
            total_cost += cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        if total_gas < total_cost:
            return -1
        else:
            return start
        
import unittest

class TestGasStation(unittest.TestCase):
    def test_can_complete_circuit(self):
        s = Solution()
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(s.canCompleteCircuit(gas, cost), 3)

    def test_cannot_complete_circuit(self):
        s = Solution()
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        self.assertEqual(s.canCompleteCircuit(gas, cost), -1)

    def test_single_station(self):
        s = Solution()
        gas = [1]
        cost = [1]
        self.assertEqual(s.canCompleteCircuit(gas, cost), 0)


 

if __name__ == '__main__':
    unittest.main()