import socket  # socket
from json import dumps, loads  # JSON 파싱 함수

class soc:
    def __init__(self, host: str, port: int, recv_limit: int = 1024):
        # 생성자
        self.host = host
        self.port = port
        self.recv_limit = recv_limit
        # init(host: str, port: int, recv_limit int= 1024): 소켓 생성 연결
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPv4, TCP
        self.socket.bind((self.host, self.port))
        print("서버 소켓 생성")

        self.socket.listen()  # 소켓 신호 수신 대기
        print("서버 소켓 수신")

        # 연결된 클라이언트 소켓 생성
        self.client_socket, self.client_addr = self.socket.accept()  # 소켓 신호 수신
        print("클라이언트 주소 {addr}".format(addr=self.client_addr))

    # send(data: str): 문자열 테이터 송신
    def send_string(self, data: str) -> None:
        bytes_data = data.encode()  # 문자열 >> 바이트 인코딩
        self.send(bytes_data)

    def send_json(self, data: dict) -> None:
        string_data = dumps(data)  # JSON >> 문자열 직렬화
        bytes_data = string_data.encode()  # 문자열 >> 바이트 인코딩
        self.send(bytes_data)

    # send(data: bytes): 바이트 테이터 송신
    def send(self, data: bytes) -> None:
        self.socket.sendall(data)

    # recv() -> byte: 바이트 데이터 수신
    def recv(self) -> bytes:
        return self.client_socket.recv(self.recv_limit)

    # recv() -> str: 스트링 데이터 수신
    def recv_string(self) -> str:
        bytes_data = self.recv()
        string_data = bytes_data.decode()
        return string_data

    # recv() -> json: json 데이터 수신
    def recv_json(self) -> dict:
        bytes_data = self.recv()
        dict_data = loads(bytes_data)
        return dict_data

# main
# host: 127.0.0.1, port: 50000
if __name__ == '__main__':
    host = "127.0.0.1"
    port = 50000
    #byte_data = b'My name is Darth Vador'
    a = soc(host, port)
    data = a.recv() # 클라이언트 데이터 수신
    print('data: {}'.format(data))
