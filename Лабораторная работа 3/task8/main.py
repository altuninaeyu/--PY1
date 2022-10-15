money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


# TODO Оформить решение
def living(money_capital, salary, spend, increase):
    month = 0
    while money_capital >= spend:
        money_capital = money_capital - spend + salary
        spend *= (1+increase)
        month += 1
    return (month)

month = living(money_capital, salary, spend, increase)
print(month)
