def perform_operation(num1, num2, operation):
    """
    perform the sepecified arithmetric operation on two numbers.

    parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation(string): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    returns:
    float or str: The result of the operation, or an erro message if the operation is invalid.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"