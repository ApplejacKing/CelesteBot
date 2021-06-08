import numpy as np
from PIL import ImageGrab
import time
import cv2
from scipy import signal


class MaskSearch:
    def __init__(self):
        self.screen_bbox = (0, 35, 964, 572)
        self.lower_red = np.array([100, 150, 50])
        self.upper_red = np.array([150, 200, 200])
        self.mh_mask = np.ones((50, 36), dtype=int)

    def search_MH(self):
        screen =  np.array(ImageGrab.grab(bbox=self.screen_bbox))
        screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
        temp_res = signal.convolve2d(mask, self.mh_mask, boundary='symm', mode='same')
        mh_center = np.unravel_index(temp_res.argmax(), temp_res.shape)[::-1]
        #self.show(screen, mask, mh_center)
        return mh_center

    def show(self, screen, mask, mh_center):
        res = cv2.bitwise_and(screen, screen, mask=mask)
        res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        color = (0, 0, 255)
        cv2.circle(res_rgb, mh_center, 15, color, 1)
        while True:
            cv2.imshow('res_rgb', res_rgb)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break