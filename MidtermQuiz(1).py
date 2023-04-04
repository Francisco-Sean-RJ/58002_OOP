class TemperatureConversion:
    def __init__(self):
        self.temp = float(input("Enter the temperature: "))
        self.unit = input("Enter the unit (C, F, K, or A): ")

    def celsiustofahrenheit(self):
        return (self.temp * 9/5) + 32

    def celsiustokelvin(self):
        return self.temp + 273.15

    def fahrenheittocelsius(self):
        return (self.temp - 32) * 5/9

    def fahrenheittokelvin(self):
        return (self.temp + 459.67) * 5/9

    def kelvintocelsius(self):
        return self.temp - 273.15

    def kelvintofahrenheit(self):
        return (self.temp * 1.8) - 459.67

    def display(self):
        if self.unit == "C":
            print("in Fahrenheit is:", self.celsiustofahrenheit(), "in Kelvin is:", self.celsiustokelvin())
        elif self.unit == "F":
            print("in Celsius is:", self.fahrenheittocelsius(), "in Kelvin is:", self.fahrenheittokelvin())
        elif self.unit == "K":
            print("in Celsius is:", self.kelvintocelsius(), "in Fahrenheit is:", self.kelvintofahrenheit())
        elif self.unit == "A":
            print("in Fahrenheit is:", self.celsiustofahrenheit(), "in Kelvin is:", self.celsiustokelvin())
            print("in Celsius is:", self.fahrenheittocelsius(), "in Kelvin is:", self.fahrenheittokelvin())
            print("in Celsius is:", self.kelvintocelsius(), "in Fahrenheit is:", self.kelvintofahrenheit())

conv = TemperatureConversion()

conv.display()


