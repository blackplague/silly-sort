from util import value_unit_sorter

test_me = ['2345Mb', '16 Kb', '256', '1Tb', '12b', '8Gb']

print(f'Original: {test_me}')
print(f'Sorted  : {sorted(test_me, key=value_unit_sorter)}')
