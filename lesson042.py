#FIFO: First item we Insert will be the First we take Out
class Queue:

    def __init__(self):
        # Use one stack for the operations
        self.stack = []

    # Adding an item to the queue is O(1) operation
    def enqueue(self, data):
        self.stack.append(data)

    # NOTE: We use 2 stacks again but instead of explicitly defining the second stack we
    # use the call-stack of program (stack memory or execution stack)
    def dequeue(self):

        # Base case for the recursive method calls the first item
        # is the call-stack of program (stack memory or execution stack)
        if len(self.stack)==1:
            return self.stack.pop()

        # We keep popping the items until we find the last on
        item = self.stack.pop()

        # We call the method recursively until we find the first item we have inserted
        dequeued_item = self.dequeue()

        # After we find the item we have to reinsert the items one by one
        self.stack.append(item)

        # This is the item we are looking for (this is what have been popped off in the
        # stack.size() == 1 section
        return dequeued_item


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

