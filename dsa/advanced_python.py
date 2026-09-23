import time


def timer(func):
    """Measure and print the execution time of a function."""

    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Execution time: {elapsed_time:.4f} seconds")

    return wrapper


@timer
def slow_function():
    """Simulate a slow function for testing the timer decorator."""
    time.sleep(2)
    print("Function finished!")


slow_function()


def count_up_to_three():
    """Generate the numbers 1, 2, and 3 one at a time."""
    yield 1
    yield 2
    yield 3


for number in count_up_to_three():
    print(number)


def fibonacci(limit):
    """Generate Fibonacci numbers up to the specified limit."""
    a = 0
    b = 1

    for _ in range(limit):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)


class FileManager:
    """Manage opening and closing a file using a context manager."""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()


with FileManager("example.txt", "w") as file:
    file.write("Hello from my context manager!")
