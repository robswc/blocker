from libs import essentials as e

open = [1, 2, 3, 4, 5]
high = [1, 2, 3, 4, 5]
low = [1, 2, 3, 4, 5]
close = [1, 2, 3, 4, 5]

sma = e.Series()
sma_2 = e.Series()

def study(title, open, high, low, close):
    sma.update(e.sma(e.id(), close, 9))



for i in range(0, 100):
    close.append(close[-1] + 1)
    study('RSI Strategy', open, high, low, close)