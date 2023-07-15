from zmq import Context, PULL
from logging import DEBUG, basicConfig, getLogger

def gather(port: int) -> None:

    basicConfig(
        filename="log/log.txt",
        filemode="wt",
        level=DEBUG
    )
    logger = getLogger()

    address = "tcp://*:{port}".format(port=port)

    context = Context()
    socket = context.socket(PULL)
    socket.bind(address)

    new_data = socket.recv_string()
    logger.debug(new_data)
