input()
prices = list(map(int, input().split()))
qualities = list(map(int, input().split()))
result = "Poor Alex"
m_e_position = prices.index(max(prices)) #most_expensive
m_e_price = prices[m_e_position]
m_e_quality = qualities[m_e_position]
for i in range(0, len(prices)):
    if prices[i] == m_e_price and qualities[i] > m_e_quality:
        m_e_quality = qualities[i]
for i in range(0, len(prices)):
    if prices[i] < m_e_price and qualities[i] > m_e_quality:
        result = "Happy Alex"
print(result)

