def function MaxSubseqSum(N, alist):
	ThisSum = 0
	MaxSum = 0
	for i in range(N):
		ThisSum += alist[i]
		if (ThisSum > MaxSum):
			MaxSum = ThisSum
		elif ThisSum < 0:
			ThisSum = 0
	return MaxSum

if __name__ == '__main__':
	print(MaxSubseqSum(6, [-2,11,-4,13,-5,-2]))