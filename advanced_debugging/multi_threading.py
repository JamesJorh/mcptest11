# 多线程调试示例
import threading

def worker():
    print('线程执行中...')

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()