import numpy as np
import cv2

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# 入力画像の読み込み
img = cv2.imread('si.jpg')

## TODO
gray =              # cv2.cvtColorメソッドを利用する

## TODO

# 結果を出力
cv2.imwrite('gray.jpg', gray)

# 入力画像の読み込み
img = cv2.imread('si.jpg')

## TODO
hsv =              # cv2.cvtColorメソッドを利用する

## TODO

# 結果を出力
cv2.imwrite('hsv.jpg', hsv)