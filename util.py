import re

from typing import Optional


def to_bytes(value: int, unit: Optional[str]):
    if unit == 'b' or unit is None:
        m = 0
    elif unit == 'Kb':
        m = 1
    elif unit == 'Mb':
        m = 2
    elif unit == 'Gb':
        m = 3
    elif unit == 'Tb':
        m = 4
    elif unit == 'Pb':
        m = 5
    else:
        raise Exception(f'Unknown unit: {unit}')

    b = value * pow(1024, m)
    # print(f'value={value}, unit={unit}, bytes={b}')

    return b


def value_unit_sorter(value_unit_str: str):
    r = re.compile('(?P<value>\d*) ?(?P<unit>(K|M|G|T|P)?b)?')

    m = r.match(value_unit_str)

    vs, u = m.groupdict()['value'], m.groupdict()['unit']
    if not vs.isdigit():
        raise TypeError(f'Value is not digits, value = {vs}')
    else:
        v = int(vs)

    return to_bytes(value=v, unit=u)
