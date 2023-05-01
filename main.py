import os
import re
import PySimpleGUI as sg
import requests

class ImageDownloader:
    """画像をダウンロードし、保存するクラス"""
    def __init__(self,url=None,save_dir=None,url_all=None,file_name=None):
        self.url = url
        self.save_dir = save_dir
        self.url_all = url_all
        self.file_name = file_name

    def download_image(self,url,save_dir):
        """画像をダウンロードし、保存する関数"""
        try:
            # URLから画像をダウンロード
            response = requests.get(url)
            raw_data = response.content
            # ファイル名を生成
            file_name = url.split("/")[-1]
            # ファイルパスを生成
            file_path = os.path.join(save_dir, file_name)
            # ファイルを保存
            with open(file_path, mode="wb") as f:
                f.write(raw_data)
            return file_path
        except:
            return None
    
    def download_all_images(self,url, save_dir):
        """ページ全体の画像をダウンロードし、保存する関数"""
        try:
            # URLからページ全体をダウンロード
            response = requests.get(url)
            html = response.text
            
            # 画像URLを含むimageタグを取得
            img_tags = re.findall(r'<img.+?src="(.+?)"', html)
            
            # 画像をダウンロード
            for img_url in img_tags:
                # URLから画像をダウンロード
                response = requests.get(img_url)
                raw_data = response.content
                
                # ファイル名を生成
                self.file_name = img_url.split("/")[-1]
                # ファイルパスを生成
                file_path = os.path.join(save_dir, self.file_name)
                # ファイルを保存
                with open(file_path, mode="wb") as f:
                    try:    
                        f.write(raw_data)
                        # ダウンロードした画像のURLを表示
                        image_downloader.window["-output_url_all-"].print(self.file_name)
                    except:
                        pass

            return True
        except:
            return False


class GUIView:
    def __init__(self):
    # GUIのレイアウト
        layout = [
            [sg.Frame("フォルダパスの入力", [
                [sg.Input(size=(45, 1), key="-input_folder_path-"),sg.FolderBrowse("参照")]
            ])],
            [sg.Frame("画像のダウンロード", [
                [sg.TabGroup([
                    [sg.Tab('URLからダウンロード', [
                        [sg.Input(size=(45, 1), key="-input_url-"),sg.Button("ダウンロード",key="-download-")],
                        [sg.Multiline(size=(70, 5), key="-output_url-", autoscroll=True)]
                    ]),
                    sg.Tab('ページ全体からダウンロード', [
                        [sg.Input(size=(45, 1), key="-input_url_all-"),sg.Button("ダウンロード")],
                        [sg.Multiline(size=(70, 5), key="-output_url_all-", autoscroll=True)]
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
                    # URLから画像をダウンロード
                image_manager.url = values["-input_url-"]
                image_manager.save_dir = values["-input_folder_path-"]
                file_path = image_manager.download_image(image_manager.url,image_manager.save_dir)
                if file_path:
                    # ダウンロードした画像のURLを表示
                    self.window["-output_url-"].print(image_manager.url)
                    # ダウンロードが完了した旨のポップアップメッセージを表示
                    sg.popup(f"{file_path}をダウンロードしました。")
                else:
                    sg.popup("ダウンロードに失敗しました。URLを確認してください。")
            elif values["-input_url_all-"]:
                # ページ全体から画像をダウンロード
                image_manager.url_all = values["-input_url_all-"]
                if image_manager.download_all_images(image_manager.url_all, values["-input_folder_path-"]):
                    # ダウンロードが完了した旨のポップアップメッセージを表示
                    sg.popup(f"{image_manager.url_all}からすべての画像をダウンロードしました。")
                else:
                    sg.popup("ダウンロードに失敗しました。URLを確認してください。")


        # ウィンドウを閉じる
        self.window.close()

if __name__ == "__main__":
    image_manager = ImageDownloader()
    image_downloader = GUIView()
    image_downloader.main()