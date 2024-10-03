
def safe_divide(numerator, denominator):
    
    try:
        
        num = float(numerator)
        dnom = float(denominator)
        result = num / dnom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

