import asyncio
import time

def test_call_soon(loop):
   print('call_soon method is executed')
   loop.stop()

def event_loop():
    """
    Event-loop is a functionality to handle all the events in a computational code.
    It acts round the way during the execution of whole program
    and keeps track of the incoming and execution of events.
    The Asyncio module allows a single event loop per process.
    """
    myloop = asyncio.get_event_loop()
    myloop.call_soon(test_call_soon, myloop)
    myloop.call_soon(test_call_soon, myloop)
    myloop.run_forever()
    myloop.close()

def futures():
    async def Myoperation(future):
        print("start")
        await asyncio.sleep(2)
        future.set_result('Future Completed')

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(Myoperation(future))
    try:
       loop.run_until_complete(future)
       print(future.result())
    finally:
       loop.close()

def coroutines():
    """
    The concept of coroutines in Asyncio is similar to the concept of standard Thread object under threading module.
    This is the generalization of the subroutine concept.
    A coroutine can be suspended during the execution so that it waits for the external processing
    and returns from the point at which it had stopped when the external processing was done.
    """
    async def Myoperation():
        print("First Coroutine")

    loop = asyncio.get_event_loop()
    try:
       loop.run_until_complete(Myoperation())
       print("end coroutines")

    finally:
       loop.close()



if __name__ == "__main__":
    futures()

