# import time
def gen_prime(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	arr = []
	for i in range(2,len(prime)):
		if prime[i]:
			arr.append(i)
	return arr
def check_val(arr):
	size = len(arr)
	for i in range(size-1):
		if arr[i] == arr[i+1]:
			print("Same "+str(arr[i]))
	return "Good"


def go(N, parr):

	d = {}
	d2 = {}
	arr = []

	for i in range(N):
		arr.append([0 for i in range(2)])

	arr[0][0] = parr[0]
	arr[0][1] = parr[1]
	arr[1][0] = parr[1]
	arr[1][1] = parr[2]
	d[parr[0]*  parr[1]] = 1
	d[parr[2]*  parr[1]] = 1
	
	pt1 = 1
	pt2 = N-2
	mm = 0
	# intt = time.time()
	for pt1 in range(2,N-1):
		if arr[pt1-1][1]!=arr[pt1-2][0] and arr[pt1-1][1]!=arr[pt1-2][1]:
			arr[pt1][0] = arr[pt1-1][1]
		else:
			arr[pt1][0] = arr[pt1-1][0]

		for i in range(max(3,d2.get(arr[pt1][0], -1)),len(parr)):
			if i>mm:
				mm=i
			if d.get(parr[i]*arr[pt1][0])==None and parr[i]!=arr[pt1][0] and (not((parr[i] in arr[pt1-1]) or (parr[i] in arr[pt1-2]))):
				arr[pt1][1]  = parr[i]
				d[arr[pt1][0] * parr[i]] = 1
				d2[arr[pt1][0]] = i+1
				break

	# fint = time.time()
	# print("TIME:",fint-intt)
	# print("max iter:",mm)		

	trunk = []
		
	if arr[-2][0]!=arr[-3][0] and arr[-2][0]!=arr[-3][1]:
		trunk.append(arr[-2][0])
	else:
		trunk.append(arr[-2][1])
	if arr[0][0]!=arr[1][0] and arr[0][0]!=arr[1][1]:
		trunk.append(arr[0][0])
	else:
		trunk.append(arr[0][1])

	arr[-1][0] = trunk[0]
	arr[-1][1] = trunk[1]


		
		# ind+=1
		# print(arr)
	return arr
parr = (gen_prime(315000))
# print(parr[-1],parr[-2],parr[-1]*parr[-2]<10**9,len(parr))

# print(parr[-1])

arf = go(50000, parr)

for x in range(int(input())):

	# iffd = False
	# for i in arf:
	# 	for j in i:
	# 		if j==0:
	# 			print("True")
	# 			iffd = True
	# 			break
	# 	if iffd:
	# 		break


	# print(len(arf))
	N = int(input())
	if N<50000:
		ara = arf[:N-1]
		# print(ara)

		a_10 = ara[-1][0]
		a_11 = ara[-1][1]
		a_20 = ara[-2][0]
		a_21 = ara[-2][1]
		a10 = ara[0][0]
		a11 = ara[0][1]
		a20 = ara[1][0]
		a21 = ara[1][1]
		uni1 = 0
		if a10!=a20 and a10!=a21:
			uni1 = a10
		else:
			uni1 = a11

		uni2 = 0
		if a_10!=a_20 and a_10!=a_21:
			uni2 = a_10
		else:
			uni2 = a_11

		ara.append([uni1,uni2])

	else:
		ara = arf

	# print(" ".join(str(v[0]*v[1]) for v in ara))
	print(" ".join(str(i[0]*i[1])  for i in ara ))



# print("Done")
# print(arf[:10],"\n",arf[-10:])

# arf.sort()

# for i in range(len(arf)-1):
# 	if arf[i]==arf[i+1]:
# 		print("BAD")
# 		break
# for x in range(int(input())):



# 	N = int(input())
# 	if N<50000:
# 		ara = arf[:N-1]
# 		# print(ara)

# 		a_10 = ara[-1][0]
# 		a_11 = ara[-1][1]
# 		a_20 = ara[-2][0]
# 		a_21 = ara[-2][1]
# 		a10 = ara[0][0]
# 		a11 = ara[0][1]
# 		a20 = ara[1][0]
# 		a21 = ara[1][1]
# 		uni1 = 0
# 		if a10!=a20 and a10!=a21:
# 			uni1 = a10
# 		else:
# 			uni1 = a11

# 		uni2 = 0
# 		if a_10!=a_20 and a_10!=a_21:
# 			uni2 = a_10
# 		else:
# 			uni2 = a_11

# 		ara.append([uni1,uni2])

# 	else:
# 		ara = arf

# 	# print(" ".join(str(v[0]*v[1]) for v in ara))
# 	print(ara[:4], ara[-4:])

# 	aff = []

# 	for i in ara:
# 		aff.append(i[0]*i[1])

# 	# print(" ".join(str(v) for v in aff))

# 	aff.sort()

# 	print(check_val(aff))
























