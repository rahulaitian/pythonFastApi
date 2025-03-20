class CustomError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def check_value(value):
    if value < 0:
        raise CustomError("Value cannot be negative!")
    elif value == 0:
        raise CustomError("Value cannot be zero!")
    else:
        print(f"Value is valid: {value}")


try:
    check_value(-5)
except CustomError as e:
    print(f"Caught an exception: {e}")
