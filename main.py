#If able to get multiple pics of girl:D can probably more precisely capture her.
import numpy as np
from PIL import ImageGrab
import time
import cv2

def main():
    template = cv2.imread('Girl.png', 0)
    w, h = template.shape[::-1]
    
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
        
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,35,964,572)))
        screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        #new_screen = process_img(screen)
        
        cv2.imshow('screen', screen_rgb)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
