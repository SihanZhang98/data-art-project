import time,datetime
from PIL import ImageGrab
import os

d1 = datetime.date.today()
end_h = 13
end_m= 28
base_dir = r"D:\Python\data_project\screenshots"

endTime = datetime.datetime(2023,d1.month,d1.day,end_h,end_m)
num=0
while datetime.datetime.now()<endTime:
    img = ImageGrab.grab()
    time.sleep(10)
    img_new = ImageGrab.grab()
    if img!=img_new:
        curr_datetime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        img_new.save(os.path.join(base_dir,curr_datetime)+".png")
        print("ok"+str(num))
        num+=1

print('finish')
    


