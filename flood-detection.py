import cv2  
from tkinter import filedialog
path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'),("Image File","jpeg"),("Image File",".png")])
img_cv = cv2.imread(path)
img=cv2.cvtColor(img_cv,cv2.COLOR_BGR2RGB)
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def rescaleFrame(frame, scale=0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
rescale=rescaleFrame(img)
gray=get_grayscale(rescale)

cv2.imshow("Display window",gray)
k = cv2.waitKey(0)