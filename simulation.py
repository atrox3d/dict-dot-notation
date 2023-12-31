from typing import Any
from dec import tabbedlogdecorator

class AttDict(dict):

    @tabbedlogdecorator()
    def __setattr__(self, item, value):
        print(f'    call self.__setitem__({item}, {value})')
        return self.__setitem__(item, value)
    
    @tabbedlogdecorator(tabs=2)
    def __setitem__(self, __key: Any, __value: Any) -> None:
        print(f'         return super().__setitem__({__key}, {__value})')
        return super().__setitem__(__key, __value)

    @tabbedlogdecorator()
    def __getattr__(self, item):
        print(f'     return self.__getitem__({item})')
        return self.__getitem__(item)
    
    @tabbedlogdecorator(tabs=2)
    def __getitem__(self, __key: Any) -> Any:
        print(f'        return super().__getitem__({__key})')
        return super().__getitem__(__key)

    __delattr__ = tabbedlogdecorator()(dict.__delitem__)
    
def main():
    ad = AttDict(a=4, b=6)

    print(f'{ad["a"]=}')
    print(f'{ad.a=}')
    print(f'{ad.b=}')
    try:
        print(ad.d)
    except Exception as e:
        print(repr(e))
    
    ad.x =  1
    print(f'{ad.x=}')

    del ad.x
if __name__ == '__main__':
    main()