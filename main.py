import os
import urllib.request
import re
import PySimpleGUI as sg

class ImageDownloader:
    def __init__(self, url, save_dir):
        self.url = url
        self.save_dir = save_dir
    
    def download_image(self):
        """画像をダウンロードし、保存する関数"""
        try:
            # URLから画像をダウンロード
            with urllib.request.urlopen(self.url) as u:
                raw_data = u.read()
            # ファイル名を生成
            file_name = self.url.split("/")[-1]
            # ファイルパスを生成
            file_path = os.path.join(self.save_dir, file_name)
            # ファイルを保存
            with open(file_path, mode="wb") as f:
                f.write(raw_data)
            return file_path
        except:
            return None
    
    def download_all_images(self):
        """ページ全体の画像をダウンロードし、保存する関数"""
        try:
            # URLからページ全体をダウンロード
            with urllib.request.urlopen(self.url) as u:
                html = u.read().decode()
            # 画像URLを含むimageタグを取得
            img_tags = re.findall(r'<img.+?src="(.+?)"', html)
            # 画像をダウンロード
            for img_url in img_tags:
                # URLから画像をダウンロード
                with urllib.request.urlopen(img_url) as u:
                    raw_data = u.read()
                # ファイル名を生成
                file_name = img_url.split("/")[-1]
                # ファイルパスを生成
                file_path = os.path.join(self.save_dir, file_name)
                # ファイルを保存
                with open(file_path, mode="wb") as f:
                    f.write(raw_data)
            return True
        except:
            return False


class GUIView:
    def __init__(self):
    # GUIのレイアウト
        layout = [
            [sg.Frame("ファイルパスの入力", [
                [sg.Input(size=(45, 1), key="-input_folder_path-"),sg.FolderBrowse("参照")]
            ])],
            [sg.Frame("画像のダウンロード", [
                [sg.TabGroup([
                    [sg.Tab('URLからダウンロード', [
                        [sg.Input(size=(45, 1), key="-input_url-"),sg.Button("ダウンロード",key='-download-')],
                        [sg.Multiline(size=(70, 5), key="output_url", autoscroll=True)]
                    ]),
                    sg.Tab('ページ全体からダウンロード', [
                        [sg.Input(size=(45, 1), key="-input_url-_all-"),sg.Button("ダウンロード")],
                        [sg.Multiline(size=(70, 5), key="output_url_all", autoscroll=True)]
                    ])]
                ])]
            ])]
        ]
            # ウィンドウを作成
        self.window = sg.Window("GUI", layout)

    def main(self):
        

        # イベントループ
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "-download-":
                pass
            elif values["-input_url-_all-"]:
                pass


        # ウィンドウを閉じる
        self.window.close()

if __name__ == "__main__":
    image_downloader = GUIView()
    image_downloader.main()