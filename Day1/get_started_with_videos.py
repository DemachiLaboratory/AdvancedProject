import numpy as np
import cv2

## TODO
# 動画を撮影するため
cap = 

# 動画のコーデックを指定するための4バイトのコードです(Windows OSの場合は'DIVX')
fourcc = 

# 動画ファイルとして保存するため
out = 

while( ): # Trueが返ってくるか見ることでcap初期化の成功を確認できる
    # フレームを取得
    ret, frame = 
    if ret == True: # フレームの読み込みが正しく行われれば True を返す
        frame = cv2.flip(frame, 0)
        
        # 動画を保存する
        out.write(frame)
        
        # フレームを表示する
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
## TODO

# 撮影終了後にビデオ撮影を解放することを忘れないでください
cap.release()
out.release()
cv2.destroyAllWindows()