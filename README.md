# PyImageDownloader

PyImageDownloaderは、PythonとPySimpleGUIを使用して作られた便利な画像ダウンローダーです。


![PyImageDownloader](https://user-images.githubusercontent.com/124559210/236590781-a2266cd0-68dc-4dd6-be44-f6104e7d919d.jpg)

# 特徴
画像をダウンロードできます
URLで指定したページ内の画像を一括でダウンロードできます
画像を連番でダウンロードできます

# 必要条件
Python 3.10.5以上

PySimpleGUI 4.60.4
    pip install PySimpleGUI

requests 2.29.0
    pip install requests



# 使い方
PyImageDownloaderを実行します。
「URL」欄に画像をダウンロードしたいページのURLを入力します。
「保存先ディレクトリ」欄に画像を保存するディレクトリを指定します。
「画像をダウンロードする」ボタンをクリックして、画像をダウンロードします。
画像を一括でダウンロードする
「URL」欄に画像をダウンロードしたいページのURLを入力します。
「保存先ディレクトリ」欄に画像を保存するディレクトリを指定します。
「ページ全体の画像をダウンロードする」ボタンをクリックして、ページ内の画像を一括でダウンロードします。
画像を連番でダウンロードする
「URL」欄に画像をダウンロードしたいページのURLを入力します。このとき、URL内に連番を含む部分を「*」に置き換えます。
「保存先ディレクトリ」欄に画像を保存するディレクトリを指定します。
「開始番号」欄に連番の最初の番号を入力します。
「終了番号」欄に連番の最後の番号を入力します。
「画像をダウンロードする」ボタンをクリックして、画像を連番でダウンロードします。

# クレジット
PySimpleGUI
https://pypi.org/project/PySimpleGUI/
requests
https://pypi.org/project/requests/