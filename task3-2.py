Days_in_month={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
def Next_day(day, month, year):
    next_day = day
    print(Days_in_month[month])
    if day != Days_in_month[month]:
        next_day += 1
    print (next_day)
Next_day(28, 2, 2021)