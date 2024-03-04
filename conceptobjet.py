class MyEmptyStackException(Exception):
    pass


class MyStackNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.top = None

    def add_to_stack(self, item):
        if self.size >= self.max_size:
            raise MyOutOfSizeException("La pile est pleine.")

        new_node = MyStackNode(item, self.top)
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("La pile est vide.")

        popped_item = self.top.data
        self.top = self.top.next_node
        self.size -= 1

        return popped_item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


class MyOutOfSizeException(Exception):
    pass


