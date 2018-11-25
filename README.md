# AdvancedProject_2018A2
動画解析ソフトを用いたプログラミングにより、全身や手の動画像、および肺腫瘍のＣＴ動画像を対象とし、その挙動を追跡して軌跡を描画するためのプログラム製作を学ぶ。
## Day 1
OpenCV のプログラミング
### 1. Pythonのインストール方法
#### 1.1 Anacondaのインストール
https://www.anaconda.com/download/#windows
- URLから自身のOS、環境に合ったインストーラーをダウンロードしインストールする。
- バージョンは3.6を選択する。
- インストーラーでの設定はそのままで進む。
#### 1.2 Python仮想環境を作成する(任意)
- プログラムからAnaconda Prompt を管理者として実行。
- 新しい Python 環境を作る。今のコマンドプロンプトで，次のコマンドを実行：（`your_env_name`のところに書く名前は何でもいが，あとで思い出しやすい分かりやすい名前にすること）
```
conda create -n your_env_name python=3.7
```
#### 1.3 OpenCVをインストールする
- プログラムからAnaconda Prompt を管理者として実行。
- 次のコマンドを実行し，仮想環境に切り替える：
```
activate your_env_name
```
Mac OS と Linux の場合は：
```
source activate your_env_name 
```
- 次のコマンドを実行し、OpenCVをインストールする：
```
pip install opencv-python
```
Mac OSとLinux の場合は：
```
conda config --add channels conda-forge
conda install opencv
```
#### 1.4 Python開発環境
- Jupyter notebook 
```
conda install jupyter notebook
```
- Spyder 
```
conda install spyder
```
- Visual Studio Code 
(https://code.visualstudio.com/)
- その他テキストエディタなど
Jupyter notebookがおすすめです。
