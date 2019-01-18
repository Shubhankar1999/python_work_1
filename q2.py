N, c = list(map(int, input().split()))
ls = []
for i  in range(N+1):
	ls.append(-1)
# voltage = 1,2,...,N inclusive
def goFor(x):
	print(1,x)
	return int(input())
def submitMoney():
	print(2)

low = 1
high = N

# coins = 1000
go =True
if N==1:
	mid = 1
if N==2:
	hh = goFor(1)
	if hh == 1:
		# broken .. submit money
		submitMoney()
		mid = 1
	else:
		mid = 2
if 2<N < 849:
	for i in range(1,N+1):
		hh = goFor(i)
		if hh == 1:
			submitMoney()
			mid = i
			break
while N>=999:
	mid = low + (high - low)//2

	hh = goFor(mid)
	ls[mid] = hh
	# print( "low", low, "high",high, "mid",mid)
	if hh == 0:
		# nOt broken
		low = mid+1
	else:
		# broken .. submit money
		submitMoney()
		# coins-=c

		high = mid-1
	if N>1:
		if ls[0]==1:
			mid = 1
			go = False
			break

		for u in range(1, N):
			if ls[u] == 0 and ls[u+1]==1:
				mid = u+1
				go = False
				break

	if not go:
		break





print(3, mid)





	
