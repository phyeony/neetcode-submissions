class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        seen = {}
        for i, new_temp in enumerate(temperatures):
            while stack and new_temp > stack[-1]:
                prev_lower_temp = stack.pop()
                prev_lower_tmp_idxs = seen[prev_lower_temp]

                # for each temp day in the array assign the value
                for idx in prev_lower_tmp_idxs:
                    ans[idx] = i - idx
                seen[prev_lower_temp] = []
            
            stack.append(new_temp)
            if new_temp in seen:
                seen[new_temp].append(i)
            else:
                seen[new_temp] = [i]
        return ans