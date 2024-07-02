from typing import List

def read_integers() -> List[int]:
    int_list = []
    user_input = input().split(",")
    for num in user_input:
        int_list.append(int(num))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
