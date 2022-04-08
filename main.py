import cv2
import numpy as np 
import math
 
# Lists to store the points
listPoints = []

POINT_SIZE = 5
TEXT_RATIO = 1.5
LINE_THICKNESS = 5

def draw_grid(img, grid_shape, color=(0, 255, 0), thickness=1):
    h, w, _ = img.shape
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols

    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)

    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)

    return img
 
def drawCoordinates(action, x, y, flags, userdata):
  global listPoints

  # Action to be taken when left mouse button is released
  if action==cv2.EVENT_LBUTTONUP:
    # Mark the vertex
    listPoints.append((x,y))
    cv2.circle(source, (x,y), 1, (0,0,0), POINT_SIZE, cv2.LINE_AA )
    cv2.putText(source,"({}, {})".format(str(x),str(y)),
              (x,y-10),  cv2.FONT_HERSHEY_SIMPLEX, TEXT_RATIO, (0,0,255), 4)
 
  if len(listPoints) >=2:
    p1 = listPoints[-1]
    p2 = listPoints[-2]
    cv2.line(source, p1, p2 , (0,0,0), LINE_THICKNESS)

source = np.ones((2000,2000,3))
source = draw_grid(source, (20,20), color = (0,0,0))
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCoordinates)

cv2.putText(source,"Select the Points and press 'Space' to complete the last line",
              (50, 50),  cv2.FONT_HERSHEY_SIMPLEX, TEXT_RATIO, (0,0,255), 4)

k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
#   cv2.putText(source,'''Click on the image to get the coordinates, press ESC to exit''' ,
#               (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
#               0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF

  if k == 32:
    p1 = listPoints[-1]
    p2 = listPoints[0]

    cv2.line(source, p1, p2 , (0,0,0), LINE_THICKNESS)

    print(listPoints)

  if k==99:
    source= dummy.copy()
 
cv2.destroyAllWindows()
