import PySimpleGUI as sg


def main():
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
    window = sg.Window("GUI", layout)

    # イベントループ
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-download-":
            pass
        elif values["-input_url-_all-"]:
            pass


    # ウィンドウを閉じる
    window.close()

if __name__ == "__main__":
    main()