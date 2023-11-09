import os
import cv2

path = "Images/"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

      #  print(file_name)
               
        images.append(file_name)
        
print(len(images))
frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
out=cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range (0,10):
    frame=cv2.imread(images[i])
    out.write(frame)
    cv2.imshow("o1",frame)
    if cv2.waitKey(500)==0:
        break

out.release()
print("Done")