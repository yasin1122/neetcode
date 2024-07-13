# Node Class
class Node:

    # Constructor
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# Linked List Class
class LinkedList:

    # Constructor
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # print values in the linked list
    def print_list(self) -> None:
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        
    # append O(1)
    def append(self, value) -> bool:
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True

    # pop O(n) (last item)
    def pop(self) -> Node:
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while temp:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    # prepend O(1)
    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    # pop O(1) (first item)
    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
        
    # get
    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # set value (change value at a set index)
    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # insert (new value at an index)
    def insert(self, index, value) -> bool:
        pass

    # remove (value at a given index)
    def remove(self, index) -> Node:
        pass

    # reverse (the linked list)
    def reverse(self) -> None:
        pass