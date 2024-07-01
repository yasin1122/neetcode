def get_substring(input_string: str, start: int, end: int) -> str:
    if end > len(input_string):
        return ''
    else:
        return input_string[start:end]

print(get_substring("Hello World", 6, 11))