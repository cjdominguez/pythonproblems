class ArrayStack:
    """LIFO LAST in FIRST out ...1,2,3,4,5, --> 54321"""

    def __init__(self):
        """Creates an empty stack"""
        self._data =[]  #_data focuses on nonpublic list instance

    def __len__(self):
        """returning the length (of elements) in the stack"""
        return len(self._data)

    def wholeList(self):
        """iterates through the entire list of elements """
        for x in self._data:
            print (x)

    def is_empty(self):
        """returns True if Stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Needs adds element to stack, needs e"""
        self._data.append(e)

    def top(self):
        """Return but do not remove TOP element (next element to be removed)

        if stack is_empty return Stack is Empty
        """
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]

    def pop(self):
        """returns element from top of the stack and removes it"""
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data.pop()


instance = ArrayStack()
print(instance.push(1))
print(instance.push(2))
print(instance.push(3))
print(instance.push(4))
print(instance.top(), "<-- this is the top of the stack")
print(instance.wholeList(), "<-- Extra return None from For Loop")
print(instance.__len__(), " <-- length of the Stack")
print(instance.is_empty())
print(instance.pop())
