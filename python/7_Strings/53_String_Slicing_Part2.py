def first_n_characters(s: str, n: int) -> str:
    return s[:n]

def last_n_characters(s: str, n: int) -> str:
    return s[len(s)-n:]

# do not modify below this line
print(first_n_characters("LeetCode", 3))
print(last_n_characters("LeetCode", 4))