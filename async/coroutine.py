import asyncio
import time

"""
* We say that an object is an awaitable object if it can be used in an await expression.
* Many asyncio APIs are designed to accept awaitables.
* There are three main types of awaitable objects: coroutines, Tasks, and Futures.

* Python coroutines are awaitables and therefore can be awaited from other coroutines
* Tasks are used to schedule coroutines concurrently.
"""

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(5, 'hello')
    await say_after(3, 'world')

    print(f"finished at {time.strftime('%X')}")

def custom_task(sec: int, input_str):
    return asyncio.create_task(say_after(sec, input_str))

async def main2():
    task1 = custom_task(5, "Hello")
    task2 = custom_task(3, "Wolrd")
    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed
    task1_res = await task1
    task2_res = await task2

    print(task1_res, task2_res)
    print(f"finished at {time.strftime('%X')}")

async def nested():
    return 42

async def main3():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    nested()  # so it *won't run at all*.

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main2())
    # asyncio.run(main3())
