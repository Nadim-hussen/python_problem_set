def lengthOfLongestSubstring(s):
    char_set = set()
    max_length = 0
    start = 0
    for i in range(len(s)):
        if s[i] in char_set:
            while s[start] != s[i]:
                char_set.remove(s[start])
                start += 1
            start += 1
        else:
            char_set.add(s[i])
            max_length = max(max_length, i - start + 1)
    return max_length
