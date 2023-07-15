from ast import literal_eval
from multiprocessing import Queue

def processor(get_queue: Queue, put_Queue: Queue) -> None:
    # 송신 데이터 담당
    data = literal_eval(get_queue.get())
    # 연산 처리
    processed_data = list(map(lambda x: str(x)+ str(x),data))
    data = str(processed_data)
    put_Queue.put(data)