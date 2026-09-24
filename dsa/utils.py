import argparse


def is_even(number):
    """Return True if a number is even."""
    return number % 2 == 0


def square(number):
    """Return the square of a number."""
    return number * number


def reverse_string(text):
    """Return a string in reverse order."""
    return text[::-1]


def main():
    """Run the utility functions from the command line."""
    parser = argparse.ArgumentParser(description="Career Launch utility CLI")

    parser.add_argument(
        "operation",
        choices=["even", "square", "reverse"],
        help="Operation to perform",
    )

    parser.add_argument(
        "value",
        help="Value to process",
    )

    args = parser.parse_args()

    if args.operation == "even":
        number = int(args.value)
        print(is_even(number))

    elif args.operation == "square":
        number = int(args.value)
        print(square(number))

    elif args.operation == "reverse":
        print(reverse_string(args.value))


if __name__ == "__main__":
    main()
