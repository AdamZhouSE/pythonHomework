import re
inexp=raw_input()
digits=re.findall(r"\d+",inexp)
digits.sort();
output=""
for i in range(len(digits)-1):
  output+= digits[i]+"+"
output+=digits[len(digits)-1]
print(output)