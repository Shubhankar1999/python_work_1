

def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)

def red(num,den):
	
	gc = gcd(num, den)

	return num//gc, den//gc


# print(red(1,100))
# print(red(2,50))

for tt in range(int(input())):
	arr = list(map(int, input().split()))
	N=arr[0]
	t=arr[1]
	arrmix = arr[2:]
	# print(N,t,arrmix)
	n = min(arrmix)
	if arrmix[0]<arrmix[1]:
		# n = arrmix[0]

		if t==1:
			numr = (2*N) - n - 1

		elif t==3:
			numr = (2*N) +1-n

		else:
			numr = (2*N)-1-(2*n)
		
	else:
		# n = arrmix[-1]
		if t==1:
			numr = (2*N)+1-n
		elif t==3:
			numr = (2*N) - n - 1
		else:
			numr = (2*N)-1-(2*n)

	m_ans , n_ans = red(numr, (2*N)+1)

	if m_ans ==0 or n_ans==0:
		print(1/0)

	print(m_ans,n_ans)














