FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELISIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahhrenheit):
    """
    Converts Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    celsius =  (Fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    fahrenheit = (celsius * CELISIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit
    def main():
        try:
            temp_input = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_input)
            unit = input("Is this temperature in celsius or fahrenheit? (C/F):").strip().upper()
            if unit == 'C':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            else:

                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        
        except ValueError as ve:
                print(f"Error: {ve}")
                print(f"Invalid temperature or unit. Please enter a valid numeric temperature and 'C' or 'F'.")
     



  
    if __name__ == "__main__":
        main()

