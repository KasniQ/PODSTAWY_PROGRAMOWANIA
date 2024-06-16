# 1. Write a  Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
import asyncio
async def printSentence():
    await asyncio.sleep(2)
    print("Python Exercises!")
# asyncio.run(printSentence())

# 2. Write a Python program that creates three asynchronous functions and 
# displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).

async def functionOne():
    await asyncio.sleep(1)
    print("functionOne")

async def functionTwo():
    await asyncio.sleep(2)
    print("functionTwo")

async def functionThree():
    await asyncio.sleep(3)
    print("functionThree")

# asyncio.run(functionOne())
# asyncio.run(functionTwo())
# asyncio.run(functionThree())

# 3. Write a Python program that creates an asyncio event loop and runs 
# a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.

async def numbers():
    for i in range(1,8):
        print(i)
        await asyncio.sleep(1)
# asyncio.run(numbers())

# 4. Write a Python program that implements a coroutine to 
# fetch data from two different URLs simultaneously using the "aiohttp" library.

import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
async def main():
    urls = [
        'https://www.youtube.com/',
        'https://github.com/KasniQ/PODSTAWY_PROGRAMOWANIA/tree/main/CWICZENIA_7'
    ]
    url1 = asyncio.create_task(fetch_url(urls[0]))
    url2 = asyncio.create_task(fetch_url(urls[1]))
    data1 = await url1
    data2 = await url2
    print("Data from ",urls[0], len(data1), "bytes")
    print("Data from ",urls[1], len(data2), "bytes")
# asyncio.run(main())

# 5. Write a  Python program that runs multiple asynchronous tasks 
# concurrently using asyncio.gather() and measures the time taken.
import time

async def taskOne():
    print("Task 1")
    await asyncio.sleep(5)
    print("Task 1 Finished")

async def taskTwo():
    print("Task 2")
    await asyncio.sleep(2)
    print("Task 2 Finished")

async def taskThree():
    print("Task 3")
    await asyncio.sleep(2)
    print("Task 3 Finished")

async def main():
    start = time.time()
    await asyncio.gather(taskOne(), taskTwo(), taskThree())
    finish = time.time()
    timeTaken = finish - start
    print("Time taken: ", timeTaken)
# asyncio.run(main())

# 6. Write a  Python program to create a coroutine that simulates 
# a time-consuming task and use asyncio.CancelledError to handle task cancellation.
async def taskOne():
    print("Task started")
    try:
        for i in range(10):
            print(f"Thinking... {i+1}/10")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task cancelled")
        raise
async def main():
    task = asyncio.create_task(taskOne())
    await asyncio.sleep(5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("The task has been cancelled due to environmental problems.")
# asyncio.run(main())

# 7. Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().
async def anotherTask(seconds):
    print(f'Starting task for {seconds} seconds')
    await asyncio.sleep(seconds)
    return f'Task has been completed in {seconds} seconds'
async def main():
    timeout = 8
    try:
        result = await asyncio.wait_for(anotherTask(9), timeout)
        print(result)
    except asyncio.TimeoutError:
        print(f'Timout error occured after {timeout} seconds')
# asyncio.run(main())

# 8. Write a Python program that uses asyncio queues to simulate 
# a producer-consumer scenario with multiple producers and a single consumer.

async def producer(queue, id):
    for i in range(5):
        await asyncio.sleep(2)
        item = f'Item: {id}--{i}'
        await queue.put(item)
        print(f'Producer {id} has produced -> {item}')
async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'Consumer took {item}')
        await asyncio.sleep(1)
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(5)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)
    await consumer_task
asyncio.run(main())