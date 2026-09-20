class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0
        if n == 0:
            return True
        for i in range(size):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        return False
     
            
        

        
        