import inspect


class Series:
    '''
    Series Class, essentially just a list with some extra methods!
    Will hopefully make pulling/adding data easier.
    '''
    def __init__(self):
        self.series = []

    def get(self):
        pass

    def last(self):
        return self.series[-1]

    def update(self, value):
        self.series.append(value)


def id():
    return inspect.currentframe().f_back.f_lineno

def sma(v, x, y):
    print('SUM: ', x[-y:], sum(x[-y:]))
    return round(sum(x[-y:]) / y, 2)

# def rma(v, x, y):
#     rma = ([(x + (y - 1) * hist[v]['rma'][-1] / y)])
#     hist[v]['rma'].append(rma)
#     return rma





















































# def rsi(x, y):
#     u = max(x - x[-1], 0)
#     d = max(x[-1] - x, 0)
#
#     rs = rma(u, y) / rma(d, y)
#     res = 100 - 100 / (1 + rs)
#     return res
#
#
# #
#
# pine_rsi(x, y) =>
#     u = max(x - x[1], 0)
#     d = max(x[1] - x, 0)
#     rs = rma(u, y) / rma(d, y)
#     res = 100 - 100 / (1 + rs)
#     res