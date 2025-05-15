def calculate_bmi(height:int,weight:int):
    if height<1.20 or height>2.20:
            raise Exception("身高不在偵測範圍")
    if weight<30 or weight>220:
            raise Exception("體重不在偵測範圍")
    bmi=weight/height**2
    return bmi
def main():
    try:
        height=float(input("請輸入身高(公尺)"))
        weight=int(input("請輸入體重(公斤)"))
        bmi=calculate_bmi(height,weight)
    except ValueError:
        print("輸入不符")
    except Exception as e:
        print(e)
    else:
        print(f"你的身高:{height}")
        print(f"你的體重:{weight}") 
        print(f"你的bmi:{bmi:.2f}")
    if  bmi<18.5:
        print("體重過輕")
    elif bmi<=24:
        print("體中適中")
    elif bmi<=27:
        print("輕度肥胖")
    elif bmi<=35:
        print("中度肥胖")
    else:
        print("重度肥胖")
            


if __name__ =="__main__":
    main()