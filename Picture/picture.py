# -*- coding: UTF-8 -*-

import argparse
import cv2

# 使用方法：命令行cd到脚本所在文件夹，python picture.py -i "图片路径"


def variance_of_laplacian(image):
    # 使用拉普拉斯算子提取图像边缘信息，计算边缘的平均方差
    return cv2.Laplacian(image, cv2.CV_64F).var()


# 构造参数接收图片路径
ap = argparse.ArgumentParser()
# 图片路径
ap.add_argument("-i", "--images", required=True,
                help="path of image")
# 阈值设置
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())
image = cv2.imread(args["images"])

# 取图片的灰度通道
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text = "Not Blurry"

# 如果得分比阈值低，认为是模糊
if fm < args["threshold"]:
    text = "Blurry"

# 显示图片以及得分信息
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)
