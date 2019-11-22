import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

feature_params = dict(maxCorners=255,             
                      qualityLevel=0.3,           
                      minDistance=7,             
                      blockSize=7,                
                      useHarrisDetector=False,    
                     )

lk_params = dict(winSize=(15, 15),           
                 maxLevel=2,                                
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                           10,
                           0.03
                          ),
                 flags=cv2.OPTFLOW_LK_GET_MIN_EIGENVALS,
                )

color = np.random.randint(low=0,                  # 0から
                          high=255,               # 255までの (輝度値なので0~255になります)
                          size=(255, 3)           # 255(255個の特徴点を検出したいので)×3(RGBなので)の行列を作る
                         )


ret, first_frame = cap.read()

first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

prev_points = cv2.goodFeaturesToTrack(image=first_gray,       
                                      mask=None,              
                                      **feature_params
                                     )

flow_layer = np.zeros_like(first_frame)

old_frame = first_frame
old_gray = first_gray

while True:

    # 2枚目以降のフレームの読み込み
    ret, frame = cap.read()

    # グレースケール変換
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # オプティカルフロー(正確には対応点)の検出
    next_points, status, err = cv2.calcOpticalFlowPyrLK(prevImg=old_gray,           # 前の画像(t-1)
                                                        nextImg=frame_gray,         # 次の画像(t)
                                                        prevPts=prev_points,        # 始点2次元ベクトル, 特徴点やそれに準ずる点
                                                        nextPts=None,               # 結果の2次元ベクトル
                                                        **lk_params
                                                        )

    # 正しく特徴点と対応点が検出できた点のみに絞る
    # todo: 数フレームおきに特徴点を検出しなおさないと，対応点が無くなるのでエラーになります
    good_new = next_points[status == 1]
    good_old = prev_points[status == 1]

    # フローを描く
    for rank, (prev_p, next_p) in enumerate(zip(good_old, good_new)):

        # x,y座標の取り出し
        prev_x, prev_y = prev_p.ravel()
        next_x, next_y = next_p.ravel()

        # フローの線を描く
        flow_layer = cv2.line(img=flow_layer,                 # 描く画像
                              pt1=(prev_x, prev_y),           # 線を引く始点
                              pt2=(next_x, next_y),           # 線を引く終点
                              color=color[rank].tolist(),     # 描く色
                              thickness=2,                    # 線の太さ
                             )
        # フローの特徴点を描く
        flow_layer = cv2.circle(img=flow_layer,                 # 描く画像
                                center=(prev_x, prev_y),        # 円の中心
                                radius=5,                       # 円の半径
                                color=color[rank].tolist(),     # 描く色
                                thickness=1                     # 円の線の太さ
                               )

    # 元の画像に重ねる
    result_img = cv2.add(frame, flow_layer)

    # 結果画像の表示
    cv2.imshow("frame", result_img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # 次のフレームを読み込む準備
    old_gray = frame_gray.copy()
    prev_points = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows()
cap.release()