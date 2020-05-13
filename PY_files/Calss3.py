print('====Temprature convertion====')


class Temprature:
    def __init__(self,temp):
        self.temp=temp
    def ConvertFahrenheit (self):
        return (1.8*self.temp)+32
    def ConvertCelsius (self):
        return (self.temp-32)/1.8
r1=Temprature(4)
r2=Temprature(96)
print(r1.ConvertFahrenheit())
print(r2.ConvertCelsius())




