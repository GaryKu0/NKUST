# create a function to calculate BMI return and print the result
input_values = input("輸入每天活動量 1輕度 2中度 3重度:")
height = float(input("請輸入身高(公尺)："))
weight = float(input("請輸入體重(公斤)："))


def bmi(weight, height, act):
    bmi = weight / (height * height)
    if act == 1:
        if bmi <= 18.5:
            cal = 35*weight
        elif bmi <= 24:
            cal = 30*weight
        else:
            cal = 25*weight
    elif act == 2:
        if bmi <= 18.5:
            cal = 40*weight
        elif bmi <= 24:
            cal = 35*weight
        else:
            cal = 30*weight
    elif act == 3:
        if bmi <= 18.5:
            cal = 45*weight
        elif bmi <= 24:
            cal = 40*weight
        else:
            cal = 35*weight
    bmi = round(bmi, 2)
    print("BMI為"+str(bmi))
    print("每天所需熱量"+str(cal))
    return
bmi(weight, height, int(input_values))
