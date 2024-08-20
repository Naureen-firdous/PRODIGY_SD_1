def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Conversion Program")
    
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
        
        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            print(f"{temp}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f}K.")
        
        elif unit == 'K':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            print(f"{temp}K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        
        else:
            print("Invalid unit of measurement. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    main()
