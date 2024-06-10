class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        expected = sorted(heights)
        for x in range(len(heights)):
            if heights[x] != expected[x]:
                c += 1
        return c
