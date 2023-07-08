from zmq import Context, PUSH


class soc:  # 클래스 생성
    def __init__(self, host: str, port: int, recv_limit: int = 1024):  # 클래스 시작시
        # 생성자
        self.host = host
        self.port = port
        self.recv_limit = recv_limit
        # init(host: str, port: int, recv_limit int= 1024): 소켓 생성 연결
        self.context = Context()  # context 객체 호출
        self.socket = self.context.socket(PUSH)  # PUSH 타입 소켓 생성 (단방향 송신 타입)
        # 소켓 연결
        self.socket.connect("tcp://{host}:{port}".format(host=host, port=port))  # 목적지 ip, port 지정, 소켓 연결

    # close: 소켓 연결 해제, 제거, 컨텍스트 객체 제거
    def close(self):
        self.socket.disconnect("tcp://{host}:{port}".format(host=host, port=port))  # 소켓 연결 해제
        self.socket.close()  # 소켓 제거
        self.context.term()  # 컨텍스트 제거


# main
# host: 127.0.0.1, port: 50000
if __name__ == '__main__':
    host = "localhost"
    port = 50000
    str_data = "My name is Darth Vador"
    # json_data = {"name": "My name is Darth Vador"}
    a = soc(host, port)
    a.socket.send_string(str_data)  # 서버에 송신
    a.close()
