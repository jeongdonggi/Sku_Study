from zmq import Context, PUSH
from multiprocessing import Queue, Process


def sender(host: str, port: int, queue: Queue) -> None:
    # 컨텍스트 객체 생성
    context = Context()
    # 단방향 수신용 소켓 생성ㄴ
    socket = context.socket(PUSH)

    # 주소 설정 및 단방향 수신용 소켓 연결
    send_address = "tcp://{host}:{port}".format(host=host, port=port)
    socket.connect(addr=send_address)

    data = queue.get()
    socket.send_string(data)
