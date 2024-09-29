#Define global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahreheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIIT_FACTOR
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def is_valid_temperature(temp):
    """
    Check if the temperature is a valid number.
    """

    try:
        float(temp)
        return True
    except ValueError:
        return False
    
def main():
        #prompt user for the temperature input
        temp_input = input("Enter the temperature to convert: ").strip()

        #check if the input is a valid temperature
        if not is_valid_temperature(temp_input):
            print("Invalid temperature. Please enter a numeric value.")
            return
        
        #convert the temperature input to a float
        temperature = float(temp_input)

        #Ask the user if the input temperature is in celsius or fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        #check if the user entered 'C' for celsius or 'F' for fahrenheit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahreheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
    