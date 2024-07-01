def remove_fourth_character(word: str) -> str:
    return word[:3] + word[4:]

print(remove_fourth_character("LeetCode"))