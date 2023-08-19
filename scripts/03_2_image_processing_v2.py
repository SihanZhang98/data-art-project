from PIL import Image
import os 
import random

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#read all screenshot images and masks
img_path = r'D:\Python\data_project\screenshots'
mask_path = r'D:\Python\data_project\rect_masks'
images = load_images_from_folder(img_path)
masks = load_images_from_folder(mask_path)

res = 800
crop_start_x = random.randint(0,500)

#change mask size 
for n, mask in enumerate(masks):
    masks[n] = mask.resize((res,res))

# convert mask to grayscale
for n, mask in enumerate(masks):   
    masks[n]= mask.convert('1') 

#crop image to be the same size as mask
#The scereenshots are 1920x1080 so I made the 
#cropping of the left side starts randomly from 0-500
for n, img in enumerate(images):
    images[n] = img.crop((crop_start_x,0,crop_start_x+res,res))


#make mask to be the alpha channel of the screenshot
index = 0
for(mask,img) in zip(masks,images):
    print(mask.size,img.size) #make sure they are the same size
    img.putalpha(mask)

    saving_path = os.path.join(r'D:\Python\data_project\masked_images_2',str(index)+".png")
    img.save(saving_path)  #save masked images

    index=index+1

print('finish!')