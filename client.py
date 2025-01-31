import os
import socket

# UNIXドメインソケットとデータグラム（非接続）ソケットを作成します
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバのアドレスを定義します。
# サーバはこのアドレスでメッセージを待ち受けます
server_address = './udp_socket_file'

# このクライアントのアドレスを定義します。
# サーバはこのアドレスにメッセージを返します
address = './udp_client_socket_file'

# サーバに送信するメッセージを定義します
message = b'Message to send to the client.'

# このクライアントのアドレスをソケットに紐付けます。
# これはUNIXドメインソケットの場合に限ります。
# このアドレスは、サーバによって送信元アドレスとして受け取られます。
# 既存のソケットファイルを削除（存在する場合）
if os.path.exists(address):
    os.remove(address)
sock.bind(address)


try:
    # サーバにメッセージを送信します
    message = input("what do you want ?").encode()
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # サーバからの応答を待ち受けます
    print('waiting to receive')
    # 最大4096バイトのデータを受け取ります
    data, server = sock.recvfrom(4096)

    # サーバから受け取ったメッセージを表示します
    print('received {!r}'.format(data))

finally:
    # 最後にソケットを閉じてリソースを解放します
    print('closing socket')
    sock.close()