class CountedIterator:
    def __init__(self, iterable):
        # Initialize the iterator and counter
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        # Increment the counter each time __next__ is called
        self.counter += 1
        # Fetch the next item from the iterator
        return next(self.iterator)

    def get_count(self):
        # Return the current count of iterated items
        return self.counter

    def __iter__(self):
        # The iterator protocol requires this method to return the iterator itself
        return self
