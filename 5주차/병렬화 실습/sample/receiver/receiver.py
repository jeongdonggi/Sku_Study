from zmq import Context, PULL
from multiprocessing import Queue

def receiver(port: int, queue: Queue) -> None:
    # 컨텍스트 객체 생성
    context = Context()
    # 단방향 수신용 소켓 생성
    socket = context.socket(PULL)

    # 주소 설정 및 단방향 수신용 소켓 연결
    recv_address = "tcp://*:{port}".format(port=port)
    socket.bind(addr=recv_address)

    data = socket.recv_string()
    queue.put(data)