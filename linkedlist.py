
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self, value):
        new_node = LinkedList.Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def remove(self, value):
        if self.size == 0:
            raise ValueError("LinkedList is empty")
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.value == value:
                prev_node.next = curr_node.next
                if curr_node == self.tail:
                    self.tail = prev_node
                self.size -= 1
                return
            prev_node = curr_node
            curr_node = curr_node.next
        raise ValueError("Value not found in LinkedList")
