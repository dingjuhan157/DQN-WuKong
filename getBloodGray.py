# coding=utf-8
import cv2
import time
import numpy as np
import grabscreen
import BloodCommon

def main():
    time.sleep(5)

    # 抓取屏幕灰度图
    np.savetxt('gray_image.txt', BloodCommon.get_self_energy_window().gray, fmt='%d')

    # print(gray_image.shape)

if __name__ == "__main__":
    main()