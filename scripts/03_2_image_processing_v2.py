from PIL import Image
import os 

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#read all screenshot images
img_path = r'D:\Python\data_project\screenshots'
mask_path = r'D:\Python\data_project\rect_masks'
images = load_images_from_folder(img_path)
masks = load_images_from_folder(mask_path)

res = 800
#change mask size and convert to grayscale
for n, mask in enumerate(masks):
    masks[n] = mask.resize((res,res))

for n, mask in enumerate(masks):   
    masks[n]= mask.convert('1') 

#crop image to be the same size as mask
for n, img in enumerate(images):
    images[n] = img.crop((0,0,res,res))

#masked_images = []
index = 0
for(mask,img) in zip(masks,images):
    print(mask.size,img.size)
    img.putalpha(mask)
    #save masked images
    saving_path = os.path.join(r'D:\Python\data_project\masked_images_2',str(index)+".png")
    img.save(saving_path)  
    index=index+1

print('finish!')