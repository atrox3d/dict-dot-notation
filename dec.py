def tabbedlogdecorator(tabs=0):
    _tabs = ' ' * tabs * 4

    def logdecorator(fn):
        def args2str(*args, **kwargs) -> str:
            params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
            params = ', '.join(params)
            return params

        def wrap(self, *args, **kwargs):
            params = args2str(*args, **kwargs)
            print(f'{_tabs}{fn.__name__}({params})')
            return fn(self, *args, **kwargs)
        return wrap
    return logdecorator
