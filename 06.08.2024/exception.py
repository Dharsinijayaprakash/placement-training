class NegativeNumberError(Exception):
    def __init__(root, value):
        root.value = value

    def __str__(root):
        return f"A negative number {root.value} was encountered in the list."

# Example usage
def check_list(num):
    for u in num:
        if u < 0:
            raise NegativeNumberError(u)

try:
    check_list([1, 2, -3, 4])
except NegativeNumberError as e:
    print(e)
