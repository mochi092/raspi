import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time

host = '127.0.0.1' #localhost
port = 10500   #julisuサーバーモードのポート
def main():

    p = subprocess.Popen(["./julius-start.sh"], stdout=subprocess.PIPE, shell=True) # julius起動スクリプトを実行
    pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
    print("process id is " + pid)
    time.sleep(3) # 3秒間スリープ

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port)) #サーバーモードで起動したjuliusに接続
    print("start socket")

    try:
        data = '' # dataの初期化
        killword ='' # 前回認識した言葉を記憶するための変数
        while 1:
            #print(data) # 認識した言葉を表示して確認
            if '</RECOGOUT>\n.' in data: 
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):

                    word = whypo.get('WORD')# juliusで認識したWORDをwordに入れる
                    
                    # wordを表示
                    print("word: " + word)

                    if word == '大悟':
                        if killword != '大悟':
                            #os.system("aplay '/home/pi/Music/konnichiwa.wav'")# 音声ファイルを再生
                            print("こんにちは、大悟さん")
                            killword = '大悟'

                    elif word == 'おはよう':
                        if killword != 'おはよう':
                            #os.system("aplay '/home/pi/Music/ohayo.wav'")
                            killword = 'おはよう'

                    data = '' # dataの初期化

            else:
                data += str(client.recv(1024).decode('utf-8')) #dataが空のときjuliusからdataに入れる
                #print('NotFound')# juliusに認識する言葉がない。認識していない。


    except KeyboardInterrupt:
        p.kill()
        subprocess.call(["kill " + pid], shell=True)# juliusのプロセスを終了する。
        client.close()

if __name__ == "__main__":
    main()
