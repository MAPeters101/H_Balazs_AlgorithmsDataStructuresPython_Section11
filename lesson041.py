
#FIFO: First item we Insert will be the First we take Out
class Queue:

    def __init__(self):
        # Use one stack for enqueue operation
        self.enqueue_stack = []
        # Use another stack for the dequeue operation
        self.dequeue_stack = []

    # Adding an item to the queue is O(1) operation
    def enqueue(self, data):
        self.enqueue_stack.append(data)

    # Getting items
    def dequeue(self):

        # Maybe there are no items in the stacks
        if len(self.enqueue_stack)== 0 and len(self.dequeue_stack)==0:
            raise Exception("Stacks are empty...")

        # If the dequeue stack is empty we have to add items O(N) times
        if len(self.dequeue_stack) == 0:

            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        # Otherwise we just have to pop off an item in O(1)
        return self.dequeue_stack.pop()

if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(20)

    print(queue.dequeue())

    queue.enqueue(100)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

