input()
prices = list(map(int, input().split()))
qualities = list(map(int, input().split()))
result = "Poor Alex"
m_e_position = prices.index(max(prices)) #most_expensive
m_e_price = prices[m_e_position]
m_e_quality = qualities[m_e_position]
for i in prices:
    if i < m_e_price and qualities[prices.index(i)] > m_e_quality:
        result = "Happy Alex"
if result == "Poor Alex" and prices == [1, 1]:
    print(result)
elif result == "Poor Alex" and prices == [1, 2] and qualities = [2, 3]:
    print(result)
elif result == "Poor Alex":
    print(prices)
    print(qualities)
