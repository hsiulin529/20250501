def calculate_bmi(height:int,weight:int):
    if height<1.20 or height>2.20:
            raise Exception("身高不在偵測範圍")
    if weight<30 or weight>220:
            raise Exception("體重不在偵測範圍")
    bmi=weight/height**2
    return bmi
def get_state(bmi:float)->str:
    if  bmi<18.5:
        message="體重過輕"
    elif bmi<=24:
        message="體中適中"
    elif bmi<=27:
        message="輕度肥胖"
    elif bmi<=35:
        message="中度肥胖"
    else:
        message='重度肥胖'
    return message