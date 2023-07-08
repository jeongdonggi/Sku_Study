from json import dumps, loads  # JSON 파싱 함수
import socket  # socket

class soc: #클래스 생성
    def __init__(self, host: str, port: int, recv_limit: int = 1024): # 클래스 시작시
        # 생성자
        self.host = host
        self.port = port
        self.recv_limit = recv_limit
        # init(host: str, port: int, recv_limit int= 1024): 소켓 생성 연결
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPv4, TCP

        try:
            # 연결 시도
            self.socket.connect((self.host, self.port))
            print("클라이언트 소켓 -> 서버 {host}:{port}".format(host=host, port=port))
        except Exception as exception_type:
            # 실패 -> 에러 출력 및 종료
            print(exception_type)
            print("서버와 연결 실패 및 프로그램 종료")
            exit()


    # send(data: str): 문자열 테이터 송신
    def send_string(self, data: str) -> None:
        bytes_data = data.encode()  # 문자열 >> 바이트 인코딩
        self.send(bytes_data)

    # send(data: str): json 테이터 송신
    def send_json(self, data: dict) -> None:
        string_data = dumps(data)  # JSON >> 문자열 직렬화
        bytes_data = string_data.encode()  # 문자열 >> 바이트 인코딩
        self.send(bytes_data)

    # send(data: bytes): 바이트 테이터 송신
    def send(self, data: bytes) -> None:
        self.socket.sendall(data)


    # recv() -> byte: 바이트 데이터 수신
    def recv(self) -> bytes:
        return self.socket.recv(self.recv_limit)

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
    byte_data = b'My name is Darth Vador'
    #json_data = {"name": "My name is Darth Vador"}
    a = soc(host, port)
    a.send(byte_data) #서버에 송신