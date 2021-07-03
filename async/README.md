# Asyncio
event-driven programming  
the model having the concept of event-driven programming is called asynchronous model.


## Coroutine
Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the async def statement.


![](https://github.com/tkxkd0159/TIL_python/blob/main/img/async.PNG) <br>

## Methods
* loop = `get_event_loop()` − This method will provide the event loop for the current context.

* `loop.call_later(time_delay,callback,argument)` − This method arranges for the callback that is to be called after the given time_delay seconds.

* `loop.call_soon(callback,argument)` − This method arranges for a callback that is to be called as soon as possible. The callback is called after call_soon() returns and when the control returns to the event loop.

* `loop.time()` − This method is used to return the current time according to the event loop’s internal clock.

* `asyncio.set_event_loop()` − This method will set the event loop for the current context to the loop.

* `asyncio.new_event_loop()` − This method will create and return a new event loop object.

* `loop.run_forever()` − This method will run until `stop()` method is called.