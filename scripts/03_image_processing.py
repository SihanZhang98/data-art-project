import cv2
import os 

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#read all screenshot images
img_path = r'D:\Python\data_project\screenshots'
mask_path = r'D:\Python\data_project\rect_masks'
images = load_images_from_folder(img_path)
masks = load_images_from_folder(mask_path)

res = 800
#change mask size
for n, mask in enumerate(masks):
    masks[n] = cv2.resize(mask,(res,res))

#crop image to be the same size as mask
for n, img in enumerate(images):
    images[n] = img[0:res,0:res]

#masked_images = []
index = 0
for(mask,img) in zip(masks,images):

    #make sure mask and image are the same dimension
    #and the same datatype
    print(mask.shape,img.shape)
    print(mask.dtype,img.dtype)

    #maked image with rect masks
    masked = cv2.bitwise_and(img,mask)
    cv2.imshow("img",masked)
    cv2.waitKey(0)

    #save masked images
    saving_path = os.path.join(r'D:\Python\data_project\masked_images',str(index)+".png")
    print(saving_path)
    status = cv2.imwrite(saving_path,masked)
    print(status)
    index=index+1

print('finish!')






