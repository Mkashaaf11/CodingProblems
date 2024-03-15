class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        std::stack<int> stack;
        std::vector<int> left, right, width, area;
        int n = heights.size();

        // Nearest smallest left
        for (int i = 0; i < n; ++i) {
            if (stack.empty()) {
                left.push_back(-1);
            } else if (heights[stack.top()] < heights[i]) {
                left.push_back(stack.top());
            } else {
                while (!stack.empty() && heights[stack.top()] >= heights[i]) {
                    stack.pop();
                }
                left.push_back(stack.empty() ? -1 : stack.top());
            }

            stack.push(i);
        }

        while (!stack.empty()) {
            stack.pop();
        }

        // Nearest smallest right
        for (int i = n - 1; i >= 0; --i) {
            if (stack.empty()) {
                right.push_back(n);
            } else if (heights[stack.top()] < heights[i]) {
                right.push_back(stack.top());
            } else {
                while (!stack.empty() && heights[stack.top()] >= heights[i]) {
                    stack.pop();
                }
                right.push_back(stack.empty() ? n : stack.top());
            }

            stack.push(i);
        }

        std::reverse(right.begin(), right.end());

        for (int i = 0; i < n; ++i) {
            width.push_back(right[i] - left[i] - 1);
            area.push_back(width[i] * heights[i]);
        }

        return *std::max_element(area.begin(), area.end());
    }
    
};