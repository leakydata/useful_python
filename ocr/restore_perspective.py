import os
import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def get_inner_rectangle(points):
    # Assuming points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    # Calculate the center of the points
    cx = sum(x for x, y in points) / 4.0
    cy = sum(y for x, y in points) / 4.0
    
    # Calculate the inner rectangle points by moving towards the center
    # You can adjust the factor (0.1 here) to get a rectangle closer or farther from the boundary
    inner_points = [(cx + 0.9 * (x - cx), cy + 0.9 * (y - cy)) for x, y in points]
    
    return np.array(inner_points, np.int32)

# Initialize list to store points and markers
points = []
markers = []

def onclick(event):
    global points, markers
    if event.button == 1:  # Left mouse button
        ix, iy = event.xdata, event.ydata
        if ix is not None and iy is not None:
            points.append((ix, iy))
            marker, = ax.plot(ix, iy, marker='o', markersize=5, color='red')
            markers.append(marker)
            fig.canvas.draw()

            if len(points) == 4:
                # Draw the outer polygon
                poly = plt.Polygon(points, edgecolor='yellow', fill=None)
                ax.add_patch(poly)
                
                # Calculate and draw the inner rectangle
                inner_points = get_inner_rectangle(points)
                inner_poly = plt.Polygon(inner_points, edgecolor='green', fill=None)
                ax.add_patch(inner_poly)
                
                fig.canvas.draw()

# Load your image here
img_path = r'\filepath\here'
image_data = cv2.imread(img_path)
img = image_data
image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots(figsize=(16,10))
ax.imshow(image_data)

# Get image dimensions
height, width = image_data.shape[:2]

# Set axis limits to allow 20% outside the image
ax.set_xlim([-0.2 * width, 1.2 * width])
ax.set_ylim([1.2 * height, -0.2 * height])

fig.canvas.mpl_connect('button_press_event', onclick)
plt.axis('off')
plt.show()

print("Selected Points:", points)

def contour_to_rect(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    # top-left point has the smallest sum
    # bottom-right has the largest sum
    rect[0] = pts[0]
    rect[2] = pts[2]
    # compute the difference between the points:
    # the top-right will have the minumum difference 
    # the bottom-left will have the maximum difference
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[1]
    rect[3] = pts[3]
    return rect 

def wrap_perspective(img, rect):
    # unpack rectangle points: top left, top right, bottom right, bottom left
    (tl, tr, br, bl) = rect
    # compute the width of the new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    # compute the height of the new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    # take the maximum of the width and height values to reach
    # our final dimensions
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    # destination points which will be used to map the screen to a "scanned" view
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    # calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(rect, dst)
    # warp the perspective to grab the screen
    return cv2.warpPerspective(img, M, (maxWidth, maxHeight))

scanned = wrap_perspective(img.copy(), contour_to_rect(points))
plt.figure(figsize=(16,10))
plt.imshow(scanned)
plt.axis('off')
plt.show()

filename, file_extension = os.path.splitext(img_path)
cv2.imwrite(filename + "_fixed" + file_extension, scanned)

from skimage.filters import threshold_local

def bw_scanner(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    T = threshold_local(gray, 21, offset = 5, method = "gaussian")
    return (gray > T).astype("uint8") * 255

cv2.imwrite(filename + "_fixed_bw" + file_extension, bw_scanner(scanned))


#plt.figure(figsize=(16,10))
#plt.imshow(bw_scanner(scanned), cmap='gray')
#plt.axis('off')  # to remove the axis
#plt.show()
