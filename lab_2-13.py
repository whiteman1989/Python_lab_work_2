moneys = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

m_sum = int(input("Введіть суму здачі: "))

for m in moneys:
    if(m <= 0):
        break
    if m <= m_sum:
        back = m_sum % m
        print("Даємо ", (m_sum - back)/m, " по ", m ," $")
        m_sum = back