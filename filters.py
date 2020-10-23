from util import value_unit_sorter

def lt(x):
    def comp_lt(y):
        return value_unit_sorter(y) < value_unit_sorter(x)
    return comp_lt

def gt(x):
    def comp_gt(y):
        return value_unit_sorter(y) > value_unit_sorter(x)
    return comp_gt

def comb_and(lhs, rhs):
    def comp_and(x):
        return lhs(x) and rhs(x)
    return comp_and

def comb_or(lhs, rhs):
    def comp_or(x):
        return lhs(x) or rhs(x)
    return comp_or
