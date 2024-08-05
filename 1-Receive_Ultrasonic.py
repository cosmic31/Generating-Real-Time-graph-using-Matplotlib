from cvzone.SerialModule import SerialObject
from time import sleep


arduino = SerialObject('COM5')
i = 1
while True:
    Data = arduino.getData()
    print("The Distnce == ", Data[0])
    file1 = open("myfile.txt" , "a" )
    a = str(i) + "," +  Data[0] + "\n"
    file1.write(a)
    # Closing file
    file1.close()
    i = i+1
    
    

