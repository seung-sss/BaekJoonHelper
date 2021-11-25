# 브루트포스 문제로 완전 탐색이 필요!
from itertools import combinations

def solution():
	n, m = map(int, input().split())
	card = list(map(int, input().split()))

	result = 0
	for c in combinations(card, 3):
		tmp = sum(c)
		if tmp <= m and tmp > result:
			result = tmp

	print(result)

solution()
