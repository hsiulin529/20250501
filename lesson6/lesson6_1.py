#import tools
#from tools import calculate_bmi,get_state
#import edu
#from edu.tools import calculate_bmi,get_state
#from edu import tools  
from edu.tools import calculate_bmi as a
from edu.tools import get_state as b

def main():
    try:
        height=float(input("請輸入身高(公尺)"))
        weight=int(input("請輸入體重(公斤)"))
        bmi=a(height,weight)
    except ValueError:
        print("輸入不符")
    except Exception as e:
        print(e)
    else:
        print(f"你的身高:{height}")
        print(f"你的體重:{weight}") 
        print(f"你的bmi:{bmi:.2f}")
    print(b(bmi))
            


if __name__ =="__main__":
    main()