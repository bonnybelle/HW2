# 1. Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ.
from collections import Counter

s = 'spam and eggs or eggs with spam'
cnt = Counter()
i = ''
for i in s:
    cnt[i] += 1
print(cnt)
