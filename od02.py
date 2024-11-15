class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
class Graph:

    def __init__(self):
        self.graph = {}
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def print_graph(self):
        for node in self.graph:
            print(node,'->','-> '.join(map(str, self.graph[node])))
# Стек
stack = Stack()
print('Стек')
print(f'Стек пуст: {stack.is_empty()}')
print('Добавляем в стек числа 1, 2, 2')
stack.push(1)
stack.push(2)
stack.push(2)
print(f'Стек пуст: {stack.is_empty()}')
print(f'Текущий элемент: {stack.peek()}')
print(f'Достаем из стека: {stack.pop()}')
print(f'Размер стека: {stack.size()}')
# Очередь
queue = Queue()
print('Очередь')
print(f'Очередь пуста: {queue.is_empty()}')
print('Добавляем в очередь значений д1, д2, д3, д4')
queue.enqueue('д1')
queue.enqueue('д2')
queue.enqueue('д3')
queue.enqueue('д4')
print(f'Очередь пуста: {queue.is_empty()}')
print(f'Достаем из очереди: {queue.dequeue()}')
print(f'Размер очереди: {queue.size()}')
# Граф
graph = Graph()
print('Граф')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('C', 'G')
graph.add_edge('E', 'H')
graph.add_edge('E', 'I')
graph.add_edge('G', 'J')
graph.print_graph()