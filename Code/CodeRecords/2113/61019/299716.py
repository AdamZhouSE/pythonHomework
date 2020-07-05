read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]
suffix = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
name = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
        'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
        'Twelve', 'Thirteen', 'Forteen', 'Fifteen', 'Sixteen',
        'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
ten_name = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']


def deal(n):
    r = []
    if n >= 100:
        r.append(name[n // 100])
        r.append('Hundred')
    n %= 100
    if n >= 20:
        r.append(ten_name[n // 10])
        r.append(name[n % 10])
    else:
        r.append(name[n])
    return ' '.join(r)


n = read()
raw = []
text = []
while n:
    raw.append(n % 1000)
    n //= 1000
for k, r in enumerate(raw):
    text.append(deal(r) + suffix[k])
    # print(text[-1])
text.reverse()
print(' '.join(text))
