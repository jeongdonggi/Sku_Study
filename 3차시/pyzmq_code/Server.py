from zmq import Context, PULL
from json import dumps, loads  # JSON 파싱 함수
import socket


class soc:
    def __init__(self, host: str, port: int, recv_limit: int = 1024):
        # 생성자
        self.host = host
        self.port = port
        self.recv_limit = recv_limit
        # init(host: str, port: int, recv_limit int= 1024): 소켓 생성 연결
        self.context = Context()  # context 객체 호출
        self.client_socket = self.context.socket(PULL)  # PUSH 타입 소켓 생성 (단방향 수신 타입)
        # 소켓 연결
        self.client_socket.bind("tcp://{host}:{port}".format(host=host, port=port))  # 목적지 ip, port 지정, 소켓 연결

    # close: 소켓 연결 해제, 제거, 컨텍스트 객체 제거
    def close(self):
        self.client_socket.close()  # 소켓 제거
        self.context.term()  # 컨텍스트 제거


# main
# host: 127.0.0.1, port: 50000
if __name__ == '__main__':
    host = "127.0.0.1"
    port = 50000
    a = soc(host, port)
    data = a.client_socket.recv_string()  # 클라이언트 데이터 수신
    print('data: {}'.format(data))
    a.close()
