def CalculateBMI(weight_kg:float, height_meters: float):
    bmi = weight_kg / (height_meters ** 2)
    return bmi

name = "John Doe"
height = 1.7
weight = 71

bmi = CalculateBMI(weight, height)
print("BMI of", name, "is", bmi)
if bmi < 25:
    print(name, "is not overweight")
else:
    print(name, "is overweight")
