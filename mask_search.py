import numpy as np
from PIL import ImageGrab
import time
import cv2

def main():
    
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)
        
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,35,964,572)))
        screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        #good number 100-200, 150-200, 0-200
        #even better 100-150, 150-200, 50-200
        lower_red = np.array([100, 150, 50])
        upper_red = np.array([150, 200, 200])
        
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(screen, screen, mask=mask)
        res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        threshold = 0.5
        loc = np.where(res_rgb >= threshold)
        try:
            test = list(zip(*loc[::-1]))
            bbox_top_left = (test[0][1] - 15, test[0][2] - 15)
            bbox_bottom_right = (test[0][1] + 30, test[0][2] + 50)
            color = (0, 0, 255)
            cv2.rectangle(res_rgb, bbox_top_left, bbox_bottom_right, color, 1)
        except:
            pass
        

        last_time = time.time()
        cv2.imshow('res_rgb', res_rgb)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
