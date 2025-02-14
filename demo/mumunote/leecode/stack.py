
def largestRectangleArea(heights):
    # 添加一个 0 高度柱子，便于最后清空栈
    heights.append(0)

    stack = []  # 用栈来保存柱子的索引
    max_area = 0  # 存储最大面积

    for i in range(len(heights)):
        # 当栈不为空且当前柱子比栈顶柱子低时
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]  # 弹出栈顶元素
            # 计算宽度：当前柱子索引和栈顶元素的下一个元素索引之间的距离
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        # 当前柱子索引入栈
        stack.append(i)

    return max_area

heights = [1, 2, 5, 6 ,7, 1]
print(largestRectangleArea(heights))