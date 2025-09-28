def count_substrings_k_distinct(s, k):
    from collections import defaultdict

    def helper(start, freq, unique_count):
        if start == len(s):
            return 0
        count = 0
        for i in range(start, len(s)):
            freq[s[i]] += 1
            if freq[s[i]] == 1:
                unique_count += 1
            if unique_count == k:
                count += 1
            elif unique_count > k:
                break
            count += helper(i + 1, freq.copy(), unique_count)
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                unique_count -= 1
        return count

    return helper(0, defaultdict(int), 0)

print(count_substrings_k_distinct("abcba", 2))  