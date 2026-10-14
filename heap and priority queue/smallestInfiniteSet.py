import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.seen = set()
        self.smallest = 1
       
    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.seen.remove(num)
            return num
        num = self.smallest
        self.smallest += 1
        return num

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)
     # space complexity will be o(n)
     # running time: o(log n)
  
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)