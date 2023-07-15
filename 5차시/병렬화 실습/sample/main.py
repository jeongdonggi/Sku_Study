from multiprocessing import Queue, Process

from gather.gather import gather
from generator.generator import generator
from processor.processor import processor
from receiver.receiver import receiver
from sender.sender import sender

if __name__ == "__main__":
    receiver2processor = Queue()
    processor2sender = Queue()
    host = "localhost"
    port = 50001
    port2 = 50002

    # 프로세스 생성
    generator_process = Process(target=generator, args=(host, port))
    receiver_process = Process(target=receiver, args=(port, receiver2processor))
    processor_process = Process(target=processor, args=(receiver2processor, processor2sender))
    sender_process = Process(target=sender, args=(host, port2, processor2sender))
    gather_process = Process(target=gather, args=(port2,))

    # 프로세스 시작
    generator_process.start()
    receiver_process.start()
    processor_process.start()
    sender_process.start()
    gather_process.start()

    # 프로세스 종료
    generator_process.join()
    receiver_process.join()
    processor_process.join()
    sender_process.join()
    gather_process.join()
