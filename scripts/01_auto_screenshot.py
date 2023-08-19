import time,datetime
from PIL import ImageGrab
import os

d1 = datetime.date.today()
end_h = 10
end_m= 15
base_dir = "D:\Pics"

endTime = datetime.datetime(2023,d1.month,d1.day,end_h,end_m)
num=0
while datetime.datetime.now()<endTime:
    img = ImageGrab.grab()
    time.sleep(10)
    img_new = ImageGrab.grab()
    if img!=img_new:
        img_new.save(os.path.join(base_dir,str(num)+".png"))
        print("ok"+str(num))
        num+=1

print('finish')
    


