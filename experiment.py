from typing import Any


class NormalClass:
    default = 'default'

    def __getattribute__(self, __name: str) -> Any:
        print(f'    __getattribute__({__name})')
        print(f'    calling super().__getattribute__({__name})')
        return super().__getattribute__(__name)
    
    def __getattr__(self, item):
        print(f'         __getattribute__({item}) FAILED')
        print(f"         __getattr__({item})")
        return f'attr {item} not found'

    def __getitem__(self, item):
        print(f"    __getitem__({item})")
        # return f'{item} not found'
        print(f'    calling dict.get(self, {item})')
        return dict.get(self, item, f'item {item} not found')


class SubClass(NormalClass, dict):
    pass


def main():
    instance = SubClass()
    print('print(instance.default)')
    print(f'-> {instance.default} <-')
    print()

    print('print(instance.nonexistent)')
    print(f'-> {instance.nonexistent} <-')
    print()

    print('print(instance["nonexistent"])')
    print(f"-> {instance['nonexistent']} <-")


if __name__ == '__main__':
    main()