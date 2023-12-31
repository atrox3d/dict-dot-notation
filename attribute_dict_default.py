class AttributeDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


my_dict = {'id': 1, 'website': 'bobbyhadz.com', 'topic': 'Python'}

new_dict = AttributeDict(my_dict)

print(new_dict.example)  # 👉️ None

print(new_dict.website)  # 👉️ bobbyhadz.com
print(new_dict.topic)    # 👉️ Python
