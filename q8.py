
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
			return ("Same "+str(arr[i]))
	return "Good"


def go(N, parr):
	# N = int(input())
	# 3300
	# print(len(parr))
	kk = 3300

	d = {}
	# print(parr)

	ind = 3
	arr = []

	for i in range(N):
		arr.append([0 for i in range(2)])

	
	arr[0][0] = parr[kk]
	arr[0][1] = parr[kk-1]
	arr[-1][0] = parr[kk]
	arr[-1][1] = parr[2]
	d[parr[kk]*  parr[kk-1]] = 1
	d[parr[kk]*   parr[2]] = 1
	# print(arr)

	pt1 = 1
	pt2 = N-2

	det = 0
	if N%2==0:
		det=1

	while(pt1 != pt2 - det):
		# for pt1
		# unique = 0

		# f1 = arr[pt1-1][0]
		# f2 = arr[pt1-1][1]
		# t1 = arr[pt1-2][0]
		# t2 = arr[pt1-2][1]
		if arr[pt1-1][0]!=arr[pt1-2][0] and arr[pt1-1][0]!=arr[pt1-2][1]:
			arr[pt1][0] = arr[pt1-1][0]
		else:
			arr[pt1][0] = arr[pt1-1][1]

		# arr[pt1][0] = unique
		if ind<kk:
			arr[pt1][1] = parr[ind]
			d[arr[pt1][0]*parr[ind]] = 1
			ind+=1
		else:
			for i in parr:
				if d.get(i*arr[pt1][0])==None and not(i in arr[pt1-1] or i in arr[pt1-2]):
					arr[pt1][1]  = i
					d[arr[pt1][0] * i] = 1
					break
			# arr[pt1][1] = ok
			


		
		pt1+=1

		# print(pt1-1 ,arr)

		# for pt2

		f1 = arr[(pt2+1)  %N][0]
		f2 = arr[(pt2+1)  %N][1]
		t1 = arr[(pt2+2)  %N][0]
		t2 = arr[(pt2+2)  %N][1]

		if arr[(pt2+1)%N][0] !=arr[(pt2+2)%N][0] and arr[(pt2+1)%N][0]!=arr[(pt2+2)%N][1]:
			arr[pt2][0]  = f1
		else:
			arr[pt2][0]  = f2

		# arr[pt2][0] = unique
		# print(unique, f1, f2, t1, t2)
		if ind<kk:
			arr[pt2][1] = parr[ind]
			d[arr[pt2][0] *parr[ind]] = 1
			ind+=1
		else:
			for i in parr:
				if d.get(i*arr[pt2][0] )==None and not(i in arr[(pt2+1)%N] or i in arr[(pt2+2)%N]):
					d[arr[pt2][0]  * i] = 1
					arr[pt2][1] = i
					break
			
			
		# ind+=1
		pt2-=1

		# print(pt2+1 ,arr)
	# print("Out of while")
	if N%2!=0:
		ind_x = N//2
		f1 = arr[ind_x-1][0]
		f2 = arr[ind_x-1][1]
		t1 = arr[ind_x-2][0]
		t2 = arr[ind_x-2][1]
		if f1!=t1 and f1!=t2:
			unique = f1
		else:
			unique = f2

		arr[ind_x][0] = unique

		f1 = arr[(ind_x+1)  %N][0]
		f2 = arr[(ind_x+1)  %N][1]
		t1 = arr[(ind_x+2)  %N][0]
		t2 = arr[(ind_x+2)  %N][1]

		if f1!=t1 and f1!=t2:
			unique = f1
		else:
			unique = f2

		arr[ind_x][1] = unique
		# print(arr)

	else:
		# print("?????")
		
		ind_2 = N//2
		ind_x = ind_2-1

		f1 = arr[ind_x-1][0]
		f2 = arr[ind_x-1][1]
		t1 = arr[ind_x-2][0]
		t2 = arr[ind_x-2][1]
		if f1!=t1 and f1!=t2:
			unique = f1
		else:
			unique = f2

		arr[ind_x][0] = unique

		f1 = arr[(ind_2+1)  %N][0]
		f2 = arr[(ind_2+1)  %N][1]
		t1 = arr[(ind_2+2)  %N][0]
		t2 = arr[(ind_2+2)  %N][1]

		if f1!=t1 and f1!=t2:
			unique = f1
		else:
			unique = f2

		arr[ind_2][0] = unique

		arr[ind_x][1] = parr[ind]
		arr[ind_2][1] = parr[ind]
		ind+=1
		# print(arr)
	return arr
parr = (gen_prime(31500))
# print(parr[-1],parr[-2],parr[-1]*parr[-2]<10**9,len(parr))

# print(parr[-1])

arf = go(50000, parr)
# print("Done")
print(arf)

for x in range(int(input())):



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
	print(ara[:4], ara[-4:])

	aff = []

	for i in ara:
		aff.append(i[0]*i[1])

	# print(" ".join(str(v) for v in aff))

	aff.sort()

	print(check_val(aff))
























