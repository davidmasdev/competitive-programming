# David Mas
# https://leetcode.com/problems/time-based-key-value-store/description/
# Medium
# Hash Table, String, Binary Search, Design, Weekly Contest 121
class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.timemap.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                l = mid + 1
                ans = values[mid][0]
            else:
                r = mid - 1
        return ans 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
