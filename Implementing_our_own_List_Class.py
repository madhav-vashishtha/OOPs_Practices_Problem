import ctypes

class CustomList:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = item
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        for i in range(self.size):
            result.append(str(self.array[i]))
        return "[" + ", ".join(result) + "]"

    def pop(self):
        if self.size == 0:
            return "Error: List is empty"

        last_item = self.array[self.size - 1]
        self.size -= 1
        return last_item

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            return "Error: Index out of bounds"
        return self.array[index]

    def clear(self):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)

    def insert(self, position, element):
        if position < 0 or position > self.size:
            return "Error: Invalid position"

        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.size, position, -1):
            self.array[i] = self.array[i - 1]

        self.array[position] = element
        self.size += 1

    def remove(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                return
        return "Error: Element not found"

cl = CustomList()

cl.append(10)
cl.append(20)
cl.append(30)

print(cl)        
print(len(cl))   

cl.insert(1, 15)
print(cl)        

cl.remove(20)
print(cl)        

print(cl.pop())   
print(cl)        

print(cl[1])     
print(cl[5])       

