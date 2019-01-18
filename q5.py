
# EXTRA STUFF PRINT KIYA HAI
# BUT I HAD NOT PRINTED THAT WHEN I SUBMITTED
def go(n, m):

	if n==1 and m==1:
		return [[1]], 1
	else:
		if n>m:
			arr1, x1 = go(n-1, m)
			# print("1>>>>",arr1,x1)
		else:
			arr2, x2 = go(n, m-1)
		
		if n>m:
			x=x1
			arr = arr1
			arr.append([0 for i in range(m)])
			mm = 0
			for ii in range(m):
				i = n-1
				arr2 = []
				if i>=1 and ii<=m-2:
					arr2.append(arr[i-1][ii+1])
				if i>=1 and ii>=1:
					arr2.append(arr[i-1][ii-1])
				if i>=2:
					arr2.append(arr[i-2][ii])
				if i<=n-2 and ii<=m-2:
					arr2.append(arr[i+1][ii+1])
				if i<=n-2 and ii>=1:
					arr2.append(arr[i+1][ii-1])
				if i<=n-3:
					arr2.append(arr[i+2][ii])
				if ii<=m-3:
					arr2.append(arr[i][ii+2])
				if ii>=2:
					arr2.append(arr[i][ii-2])
				for abc in range(1,6):
					if not(abc in arr2):
						final = abc
						if mm<final:
							mm=final
						break
				arr[i][ii] = final
		else:
			x=x2
			arr = arr2
			for i in arr:
				# print(i)
				i.append(0)
			mm = 0
			for i in range(n):
				ii = m-1
				arr2 = []
				if i>=1 and ii<=m-2:
					arr2.append(arr[i-1][ii+1])
				if i>=1 and ii>=1:
					arr2.append(arr[i-1][ii-1])
				if i>=2:
					arr2.append(arr[i-2][ii])
				if i<=n-2 and ii<=m-2:
					arr2.append(arr[i+1][ii+1])
				if i<=n-2 and ii>=1:
					arr2.append(arr[i+1][ii-1])
				if i<=n-3:
					arr2.append(arr[i+2][ii])
				if ii<=m-3:
					arr2.append(arr[i][ii+2])
				if ii>=2:
					arr2.append(arr[i][ii-2])
				for abc in range(1,6):
					if not(abc in arr2):
						final = abc
						if mm<final:
							mm=final
						break
				arr[i][ii] = final
		return arr,max(mm,x)



def check_val(arr):

	n = len(arr)
	m = len(arr[0])
	for i in range(len(arr)):
		for ii in range(len(arr[0])):
			arr2 = []

			if i>=1:
				arr2.append(arr[i-1][ii])
			if i<=n-2:
				arr2.append(arr[i+1][ii])
			if ii>=1:
				arr2.append(arr[i][ii-1])
			if ii<=m-2:
				arr2.append(arr[i][ii+1])

			for x in range(len(arr2)):
				for y in range(x+1,len(arr2)):
					if arr2[x]==arr2[y]:
						print(x,y,"not good")
						return False
			return True



for x in range(int(input())):

	n,m = list(map(int, input().split()))
	arrf, mmf = go(n,m)
	# print(arrf,mmf)
	mmv = 0
	for i in arrf:
		for ii in i:
			if ii>mmv:
				mmv = ii
	# print(mmf, mmv)
	print(mmv)
	prt = True
	if prt:
		for i in arrf:
			print (" ".join(str(v) for v in i))
	# val = check_val(arrf)
	# print(val, mmv==mmf)


# good = True
# for i in range(1,51):
# 	for j in range(1,51):

# 		arrf, mmf = go(i,j)
# 		mmv=0
# 		for i1 in arrf:
# 			for ii in i1:
# 				if ii>mmv:
# 					mmv = ii
# 		val = check_val(arrf)
# 		if (not val) or (mmv!=mmf):
# 			print("not so at ", i,j)
# 			good = False
			
# if good:
# 	print("All good")





	


# arr2.append(arr[i-1][ii+1])
# arr2.append(arr[i-1][ii-1])
# arr2.append(arr[i-2][ii])

# arr2.append(arr[i+1][ii+1])
# arr2.append(arr[i+1][ii-1])
# arr2.append(arr[i+2][ii])

# arr2.append(arr[i][ii+2])

# arr2.append(arr[i][ii-2])



				




