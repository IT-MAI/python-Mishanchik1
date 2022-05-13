# Очередь

class Queue:
	# Инициализация
    def __init__(self):
    	self.queue = []

    	queue = Queue()


    # Добавление элемента
    def push(self, item):
        self.queue.append(item)

    queue.push(1)

    # Удаление ЭЛЕМЕНТА
    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed

    queue.pop()
    
    # Размер
    def size(self):
    	return len(self.queue)

    print(queue.size())
    
    # Очистка
    def clear(self):
    	# queue = []
    	for i in range(len(self.queue)):
    		self.queue.pop()

    queue.clear()
    		
    # Смотрим 1 элемент
    def first(self):
    	return self.queue[0]

    print(queue.first())

    # Извлекаем k-ый элемент
    def extract(self,k):
    	# k = 4 # Удаляем к элемент 
    	if len(self.queue) >= k-1:
    		self.queue.pop(k-1)

    queue.extract(3)

# Вывод очереди
print(queue.queue) 



