import socket
import os

#AF_UNIXはUNIXドメインソケット、SOCK_DGRAMはデータグラムソケット
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバが接続を待ち受けるUNIXドメインソケットのパスを指定
server_address = './udp_socket_file'

#ソケットファイルが残っていた場合、削除
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# ソケットが起動していることを表示、ソケットを特定のアドレスに紐付け
print('starting up on {}'.format(server_address))
sock.bind(server_address)



# ソケットはデータの受信を永遠に待つ
while True:
    print('\n-----waiting to receive message-----')

    # ソケットからのデータを受信する
    # 4096は一度に受信できる最大バイト数
    data, address = sock.recvfrom(4096)

    # 受信したデータのバイト数と送信元のアドレスを表示します。
    print('received {} bytes from {}'.format(len(data), address))

    decodeMassage = data.decode()
    print("message is：" + decodeMassage)
    if(decodeMassage == "exit"):
        print('closing socket')
        sock.close()
        
    if data:
        sent = sock.sendto("next?".encode(), address)
        # 送信したバイト数と送信先のアドレスを表示します。
        print('sent {} bytes back to {}'.format(sent, address))