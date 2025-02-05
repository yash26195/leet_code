class Solution:
    def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         area = {}
#         max_area = 0
        
#         for idx1,b1 in enumerate(height):
            
#             for idx2,b2 in enumerate(height):
                
#                 if str(b1)+str(b2) or str(b2)+str(b1) not in area.keys():
#                     area[str(b1)+str(b2)] = min(b1,b2) * abs(idx1-idx2) 
#                     max_area = max(max_area,area[str(b1)+str(b2)])
#                     return max_area
#         return max_area

        n = len(height)
        area = {}
        maxarea = 0
        l,r=0,len(height)-1
        while(l<r):
            maxarea = max(maxarea,min(height[l],height[r]) * abs(l-r))
            if height[l]<height[r]:
                l+=1;
            else:
                r-=1;
                
        return maxarea