import os
import socket

# UNIXドメインソケットとデータグラム（非接続）ソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバのアドレスを定義
server_address = './udp_socket_file'

# このクライアントのアドレスを定義
address = './udp_client_socket_file'

# サーバに送信するメッセージを定義
message = b'Message to send to the client.'

# このクライアントのアドレスをソケットに紐付け
# 既存のソケットファイルを削除（存在する場合）
if os.path.exists(address):
    os.remove(address)
sock.bind(address)


try:
    while(True):
        message = input("what do you want ?").encode()
        #サーバーに送信
        sent = sock.sendto(message, server_address)

        decodeMassage = message.decode()
        print('sending：{!r}'.format(decodeMassage))

        #exitの場合は終了
        if(decodeMassage == "exit"):
            print('closing socket')
            sock.close()

        # サーバからの応答を待ち受ける
        print('\n-----waiting to receive-----')
        # 最大4096バイトのデータを受け取る
        data, server = sock.recvfrom(4096)
        decodeData = data.decode()

        # サーバから受け取ったメッセージを表示
        print('received {!r}'.format(decodeData))

finally:
    # 最後にソケットを閉じてリソースを解放します
    print('closing socket')
    sock.close()