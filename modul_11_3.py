# Задача, тема "Интроспекция"
# Цель: закрепить знания об интроспекции в Python.
# Создать персональные функции для подробной интроспекции объекта.

import inspect
from pprint import pprint

def introspection_info(obj, info = {}):
    metods = []
    attrib =[]
    type_obj = type(obj)
    pprint(dir(obj))
    attrib_metods = dir(obj)
    for attrib_metod in attrib_metods:
        if attrib_metod.__contains__('__'):
            metods.append(attrib_metod)
        else:
            attrib.append(attrib_metod)
    modul = str(inspect.getmodule(obj))
    if __name__ == "__main__" and modul == 'None':
        modul = '__main__'
    info['type'] = str(type_obj)[8:-2]
    info['attributes'] = attrib
    info['methods'] = metods
    info['module'] = modul
    if isinstance(obj, int):
        if obj%2 == 0:
            chetnost = 'число четное'
        else:
            chetnost = 'число нечетное'
        info['chetnost'] = chetnost
    return info
number_info = introspection_info(42)
print(number_info)


