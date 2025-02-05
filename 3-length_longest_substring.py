class Solution:
    # Two pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_unique(substr: str):
            return len(substr) == len(set(substr))
        
        max_substring_length = 0
        left_pointer = 0
        
        for right_pointer in range(len(s)):
            # Ensure the substring is unique by adjusting the left pointer
            while not is_unique(s[left_pointer:right_pointer + 1]):
                left_pointer += 1
            
            # Update the maximum length
            max_substring_length = max(max_substring_length, right_pointer - left_pointer + 1)
        
        return max_substring_length
