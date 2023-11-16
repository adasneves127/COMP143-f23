
def test(x: int) -> int:
    for i in range(x):
        print(i)
    return 100


def compound_interest(initial_balance: float, years: int, rate: float) -> float:
    if years == 0:
        return initial_balance
    else:
        return (1 + rate) * compound_interest(initial_balance, years - 1, rate)
    



def f(x):
    print(3*x**2 + 2*x - 1)


f(4)
f(8)
