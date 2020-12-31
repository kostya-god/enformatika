#Task1(description)
'''
Так как мы используем асинхронное программирование(модуль asyncio), мы можем проводить сразу несколько операций.
У нас есть три задачи А, В и С: посчитать факториалы для трех чисел - 2,3 и 4 оответственно. Мы запускаем нашу программу. Начинается вычисления сразу трех факториалов одновременно(параллельно).
Мы это узнаем, так как в окно вывод у нас печатается "Compute factorial(...)". После этого программа переходит в корутину sleep и "спит" 1 сек. Когда мы посчитали факториал 2, мы выполнили задачу A, поэтому на вывод мы получаем "Task A: factorial(2) = 2".
Далее программа начинает вычислять факториалы 3 и 4. Но так как задача А уже выполнена, далее мы в выводе получаем только "Task B: Compute factorial(3)..." и
"Task C: Compute factorial(3)...". Через секунду мы получаем "Task B: factorial(3) = 6". После программа вычисляет факториал 4. Т.к. первые две задачи А и В выполнены, в окне вывода мы получаем только "Task C: Compute factorial(4)...". Через секунду мы получаем "Task С: factorial(4) = 24".
'''
#Task2
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
from collections import namedtuple
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(session, service):
    async with session.get(service.url) as response:
        html = await response.json()
        return html


async def asynchronous():
    async with aiohttp.ClientSession() as session:
        fut = await asyncio.wait({fetch_ip(session, serv) for serv in SERVICES}, return_when=FIRST_COMPLETED)
        for i in fut[0]:
            a = i.result()
            for serv in SERVICES:
                try:
                    print(a[serv.ip_attr])
                except:
                    pass


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
