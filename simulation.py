from typing import Any


def logdecorator(fn):
    def wrap(*args, **kwargs):
        fn(*args, **kwargs)
    return wrap


class AttDict(dict):
    def __init__(self, *args, **kwargs):
        self.__getattr__ = logdecorator(self.__getattr__)

    def __getattr__(self, item):
        print(f'getattr( {self=}, {item=} )')
        print(f'return self.__getitem__({item})')
        return self.__getitem__(item)
    
    def __getitem__(self, __key: Any) -> Any:
        print(f'getitem( {self=}, {__key=} )')
        print(f'return super().__getitem__({__key})')
        return super().__getitem__(__key)


def main():
    ad = AttDict(a=4, b=6)

    print(ad['a'])
    print(ad.a)
    print(ad.b)
    try:
        print(ad.d)
    except Exception as e:
        print(repr(e))
if __name__ == '__main__':
    main()