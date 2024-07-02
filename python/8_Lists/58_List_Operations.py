def check_list_empty(my_list) -> bool:
    return not my_list

def check_element_in_list(my_list, element) -> bool:
    return element in my_list

# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2]))
print(check_element_in_list([1, 2], 2))