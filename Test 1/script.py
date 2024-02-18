import cv2
import numpy as np

slikaa = np.zeros((512,512,3), np.uint8)

def crtanje_kruga(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONUP:
        cv2.circle(slikaa,(x,y),30,(0,0,255),thickness=5)
        
cv2.namedWindow(winname="crtanje")
cv2.setMouseCallback("crtanje", crtanje_kruga)

while True:
    cv2.imshow("crtanje", slikaa)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()