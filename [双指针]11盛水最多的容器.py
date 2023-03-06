# 11
#   双指针，数值小的指针先走
def maxArea(height):
    start, end = 0, len(height) - 1
    m = 0
    while start <= end:
        m = max(m, min(height[start], height[end]) * (end - start))
        if height[start] < height[end]:

            start += 1
        else:

            end -= 1
    return m