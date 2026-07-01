import bisect

class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.data, num)

    def findMedian(self) -> float:
        l = len(self.data)

        if l % 2 == 0:
            mid = l // 2
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            mid = l // 2
            return self.data[mid]
            