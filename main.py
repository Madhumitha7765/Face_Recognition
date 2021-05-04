import os

def main():

    while(True):
        print("\n***********************************************************")
        print("               FACE RECOGNITION APPLICATION                ")
        print("***********************************************************")
        print("\n1.COMPARE FACES WITH PRETRAINED IMAGES")
        print("2.DETECT FACES IN LIVE WEBCAM AND RECORD THEIR STATISTICS ")
        print("3.COUNT FACES IN LIVE WEBCAM AND REPORT THEM")
        print("4.EXIT")
        ch = input("\nEnter your choice :: ")
        if int(ch)==1:
            os.system('python Faces_Image_comparison.py')
        elif int(ch)==2:
            os.system('python Webcam.py')
        elif int(ch)==3:
            os.system('python Face_counter.py')
        elif int(ch)==4:
            exit()
        else :
            print("\nPlease Enter right choice")
            continue


if __name__ == "__main__":
    main()