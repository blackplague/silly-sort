from filters import lt, gt, comb_and

test_me = ['2345Mb', '16 Kb', '256', '1Tb', '12b', '8Gb']

print(f'Original                     : {test_me}')

lt256kb = list(filter(lt("256Kb"), test_me))
gt256kb = list(filter(gt("256Kb"), test_me))

print(f'Filtered x < 256Kb           : {lt256kb}')
print(f'Filtered x > 256Kb           : {gt256kb}')

gt512b_lt4gb = list(filter(comb_and(gt('512b'), lt('4Gb')), test_me))

print(f'Filtered 512b < x and x < 4Gb: {gt512b_lt4gb}')
