#Problem description:Вывод 1-ого "проблемного" кода: 1 2 3 4 5 6 7 8 9 10 10
#Вывод 2-ого кода, демонстрирующего "проблемность" 1-ого кода:
#1 2 3 4 1 1 1 1 4 5 5 или 1 2 3 4 5 6 7 8 8 8 8 и т.д. (вывод случайный)
#Проблема кода возникает из-за того, что, когда мы добавляем в код строку time.sleep(random.randint(0, 1)), т.е. функция def thread_job() засыпает на некоторое случайное время, то разные потоки начинают менять одни и те же данные. Решаем эту проблему с помощью метода acquire(): блокируется примитив lock и выполнение блока до тех пор, пока метод  release() из другой сопрограммы не разблокирует его. Таким образом, примитивы lock  могут использоваться для предотвращения противоречивости в выходных данных, позволяя каждый раз только одному потоку изменять данные.
#Task1(Solution of the problem)
import threading
import random
import time
import sys


def thread_job():
    lock.acquire()  # mutex
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release()


lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
#Task2
import os, re
import threading
import time


def thread_job(suffix):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])


start = time.time()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
threads = [threading.Thread(target=thread_job(suffix)) for suffix in range(20, 30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)
#Task3
import time
import threading


def thread_job(b):
    global result
    result += b


n = int(input())
result = 0
start = time.time()
a = []
for i in range(n):
    a.append(i)
print(a)
threads = [threading.Thread(target=thread_job(a[i])) for i in range(len(a))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(result)
print(time.time() - start)
#Task4(время с потоками 2.901669502258301; время без потоков 2.526888847351074)
import urllib.request
import time
import threading


def thread_job(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
urls = [
        'https://www.yandex.ru', 'https://www.google.com',
        'https://habrahabr.ru', 'https://www.python.org',
        'https://isocpp.org',
    ]
threads = [threading.Thread(target=thread_job(urls[i])) for i in range(len(urls))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)
#Task5{в исходном коде не хватало круглых скобок после target=worker, т.к. worker() - это функция, а у функции есть аргументы.Если же у функции нет аргументов, пишутся просто пустые круглые скобки.}
import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker()) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)