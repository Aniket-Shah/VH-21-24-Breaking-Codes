from tkinter import filedialog
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.image import imsave

# img = cv.imread('photo/kerala_before.jpg')
path = filedialog.askopenfilename(filetypes=[("Image File", ".jpg"),("Image File", ".jpeg"),("Image File", ".png")])
# img_color = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.imread(path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# ret, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# ret, thresh3 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_TRIANGLE)

# ret, mask = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

plt.figure("OTSU")
plt.imshow(thresh2, cmap="gray")

# plt.figure("Triangle")
# plt.imshow(thresh3, cmap="gray")

plt.figure("GrayScale")
plt.imshow(gray, cmap="gray")

plt.show()