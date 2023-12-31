class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



def main():
    my_dict = {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}

    new_dict = AttributeDict(my_dict)

    print(new_dict.website)  # 👉️ bobbyhadz.com
    print(new_dict.topic)  # 👉️ Python

    new_dict.author = 'Borislav Hadzhiev'

    # 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python', 'author': 'Borislav Hadzhiev'}
    print(new_dict)

    del new_dict.author

    # 👇️ {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}
    print(new_dict)

if __name__ == '__main__':
    main()