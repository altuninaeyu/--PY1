salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def needToLive(salary, spend, months, increase):
    need_money = 0
    for month in range(0, months):
        need_money = need_money + salary - spend
        spend*=(1 + increase)
    return -need_money


need_money = needToLive(salary, spend, months, increase)
print(round(need_money))
