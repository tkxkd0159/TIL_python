# pylint: disable=invalid-name
import random
import time
from typing import Callable


TYPE = 2 # 1: decorator, 2: Observer, 3: Singleton

## Decorator ##
def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'{func.__name__} {time.perf_counter() - t}')
        return res
    return wrapper

@benchmark
def random_tree(n):
    temp = [count for count in range(n)]
    for _ in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp

class MethodTest:
    _hello = True

    def normal_foo(self, x):
        print(f"foo -> {self}, {x}")

    @classmethod
    def class_foo(cls, x):
        print(f"class_foo -> {cls}, {x}, _hello : {cls._hello}")

    @staticmethod
    def static_foo(x):
        print(f"static_foo -> {x}")
## Observer ##

class TestProperty:
    def __init__(self, name):
        self._name = name    # protected attribtue

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

#--------------------------
class SubOne:
    def __init__(self, name: str):
        self.name = name
    def update(self, message: str):
        print(f'Subscriber Type 1 update : {self.name} {message}')

class SubTwo:
    def __init__(self, name: str):
        self.name = name
    def receive(self, message: str):
        print(f'Subscriber Type 1 receive : {self.name} {message}')

class Publisher:
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None: # callback 없으면 subone의 update 할당
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message: str):
        for _, callback in self.subscribers.items():
            callback(message)

class Publisher2:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)

class EventPublisher:
    def __init__(self, events: str) -> None:
        self.subscribers = {event: dict() for event in events}

    def get_subs(self, event: str):
        return self.subscribers[event]

    def register(self, event: str, who, callback: Callable[[str], None]=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subs(event)[who] = callback

    def unregister(self, event: str, who):
        del self.get_subs(event)[who]

    def dispatch(self, event: str, message: str):
        for _, callback in self.get_subs(event).items():
            callback(message)


## Singleton ##

if __name__ == '__main__':
    if TYPE == 1:
        random_tree(10000)
        print("")

        check_method = MethodTest()
        check_method.normal_foo(1)
        check_method.class_foo(2)
        MethodTest.class_foo(2)
        check_method.static_foo(3)
        MethodTest.static_foo(3)

    elif TYPE == 2:
        test = TestProperty("first")
        print(test.name)
        test.name = "second"
        print(test.name)

        astin = SubOne("astin")
        jeff = SubOne("jeff")
        james = SubTwo("james")

        pub = Publisher()
        pub.register(astin, astin.update)
        pub.register(jeff)
        pub.register(james, james.receive)
        pub.dispatch("dispatch 1")
        pub.unregister(jeff)
        pub.dispatch("dispatch 2")

        print("")
        event_pub = EventPublisher(["lunch", "dinner"])
        event_pub.register("lunch", astin)
        event_pub.register("lunch", jeff)
        event_pub.register("dinner", astin)
        event_pub.register("dinner", james, james.receive)
        event_pub.dispatch("lunch", "it's lunch time")
        event_pub.dispatch("dinner", "it's dinner time")

    # elif TYPE == 3:



