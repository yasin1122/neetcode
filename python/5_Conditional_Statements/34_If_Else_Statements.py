def get_min(a: int, b: int) -> int:
    if a <= b:
        return a
    else:
        return b

# don't modify code below this line
print(get_min(10, 11))
print(get_min(5, -7))
print(get_min(20, 20))