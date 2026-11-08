# class Solution:
#     def get_most_seen_letter_and_count(self, count: dict):
#         most_seen_count = 0
#         most_seen_letter = 'A'
#         for key, val in count.items():
#             if most_seen_count < val:
#                 most_seen_count = val
#                 most_seen_letter = key
#         return [most_seen_count, most_seen_letter]
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = defaultdict(int)
#         most_seen_count = 0
#         most_seen_letter = s[0]
#         l = 0
#         res = 0
#         for r in range(len(s)):
#             count[s[r]] += 1
            
#             # update most seen alphabet count
#             if most_seen_letter == s[r]:
#                 most_seen_count += 1
#             else:
#                 if count[s[r]] > most_seen_count:
#                     most_seen_count = count[s[r]]
#                     most_seen_letter = s[r]
            
            
#             while (r-l+1) - most_seen_count > k:
           
#                 # delete count
#                 count[s[l]] -= 1
#                 # shift l pointer
#                 l += 1


#                 # update most seen alphabet count
#                 most_seen_count, most_seen_letter = self.get_most_seen_letter_and_count(count)
                
            
#             res = max(res, r-l+1)

#         return res
        

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_f = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            
            # If the current window is invalid, shift `l` by 1.
            # This maintains the maximum window size without shrinking it.
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                
        # The window size at the end naturally represents the maximum valid size encountered
        return len(s) - l
   