from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        old = image[sr][sc]
        que = deque()
        que.append([sr,sc])
        while que:
            new_r, new_c = que.pop()
            image[new_r][new_c] = newColor
            for new_r, new_c in zip([new_r,new_r,new_r-1,new_r+1], [new_c-1,new_c+1,new_c,new_c]):
                if new_r>=0 and new_r<len(image) and new_c>=0 and new_c<len(image[0]) and image[new_r][new_c] == old:
                    que.append([new_r,new_c])
        return image

test = [[1,1,1],[1,1,0],[1,0,1]]
solution = Solution()
ans = solution.floodFill(test,1,1,2)

# 输出打印
for lis in ans:
    print(" ".join([str(itm) for itm in lis]))