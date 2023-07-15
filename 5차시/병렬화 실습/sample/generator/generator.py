from zmq import Context, PUSH

def generator(host: str, port: int) -> None:
    # 숫자 데이터 생성
    data = list(range(10))
    # 생성 데이터 송신
    # 컨텍스트 객체 생성
    context = Context()
    # 단방향 수신용 소켓 생성
    socket = context.socket(PUSH)

    # 주소 설정 및 단방향 수신용 소켓 연결
    send_address = "tcp://{host}:{port}".format(host=host, port= port)
    socket.connect(addr=send_address)

    socket.send_string(str(data))
