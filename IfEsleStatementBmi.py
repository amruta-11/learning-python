def CalculateBMI(weight_kg:float, height_meters: float):
    bmi = weight_kg / (height_meters ** 2)
    return bmi

name = "Sam"
height = 1.7
weight = 71

samBmi = CalculateBMI(weight, height)
print("BMI of", name, "is", samBmi)
if samBmi < 25:
    print(name, "is not overweight")
else:
    print(name, "is overweight")
