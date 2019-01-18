
# EXTRA STUFF PRINT KIYA HAI
# BUT I HAD NOT PRINTED THAT WHEN I SUBMITTED
# def go(nn, mm):
	# print("??????",nn,mm)
	# arr = []
	# for i in range(nn):
	# 	arr.append([0 for i in range (mm)])

	# arr[0][0] = 1
	# n = 1
	# m = 1
	# mxm = 0
	# while n<nn or m<mm:
	# 	# print("//////////////")

	# 	if n<nn:

	# 		for ii in range(m):
	# 			i = n
	# 			arr2 = []
	# 			if i>=1 and ii<=m-2:
	# 				arr2.append(arr[i-1][ii+1])
	# 			if i>=1 and ii>=1:
	# 				arr2.append(arr[i-1][ii-1])
	# 			if i>=2:
	# 				arr2.append(arr[i-2][ii])
	# 			if i<=n-2 and ii<=m-2:
	# 				arr2.append(arr[i+1][ii+1])
	# 			if i<=n-2 and ii>=1:
	# 				arr2.append(arr[i+1][ii-1])
	# 			if i<=n-3:
	# 				arr2.append(arr[i+2][ii])
	# 			if ii<=m-3:
	# 				# print(i, ii+2)
	# 				arr2.append(arr[i][ii+2])
	# 			if ii>=2:
	# 				# print(i, ii-2)
	# 				arr2.append(arr[i][ii-2])
	# 			for abc in range(1,6):
	# 				if not(abc in arr2):
	# 					final = abc
	# 					if mxm<final:
	# 						mxm=final
	# 					break
	# 			arr[i][ii] = final
	# 		n+=1
	# 	if m<mm:
	# 		# print("''''''",m,mm)
	# 		for i in range(n):
	# 			ii = m
	# 			arr2 = []
	# 			if i>=1 and ii<=m-2:
	# 				arr2.append(arr[i-1][ii+1])
	# 			if i>=1 and ii>=1:
	# 				arr2.append(arr[i-1][ii-1])
	# 			if i>=2:
	# 				arr2.append(arr[i-2][ii])
	# 			if i<=n-2 and ii<=m-2:
	# 				arr2.append(arr[i+1][ii+1])
	# 			if i<=n-2 and ii>=1:
	# 				arr2.append(arr[i+1][ii-1])
	# 			if i<=n-3:
	# 				# print(i+2,  ii)
	# 				arr2.append(arr[i+2][ii])
	# 			if ii<=m-3:
	# 				arr2.append(arr[i][ii+2])
	# 			if ii>=2:
	# 				arr2.append(arr[i][ii-2])
	# 			for abc in range(1,6):
	# 				if not(abc in arr2):
	# 					final = abc
	# 					if mxm<final:
	# 						mxm=final
	# 					break
	# 			arr[i][ii] = final
	# 		m+=1
	# return arr,mxm
# def check_val(arr):
# 	for i in range(len(arr)):
# 		for ii in range(len(arr[0])):
# 			arr2 = []

# 			if i>=1:
# 				arr2.append(arr[i-1][ii])
# 			if i<=n-2:
# 				arr2.append(arr[i+1][ii])
# 			if ii>=1:
# 				arr2.append(arr[i][ii-1])
# 			if ii<=m-2:
# 				arr2.append(arr[i][ii+1])

# 			for x in range(len(arr2)):
# 				for y in range(x+1,len(arr2)):
# 					if arr2[x]==arr2[y]:
# 						print(x,y,"not good")
# 						return False
# 			return True

def check_val(arr):
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
def go(nn,mm):
	arr = []
	for i in range(nn):
		arr.append([0 for i in range (mm)])

	arr[0][0] = 1
	n = 1
	m = 1
	mxm = 0
	while n<nn or m<mm:
		# print("//////////////")

		if n<nn:

			for ii in range(m):
				i = n
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
					# print(i, ii+2)
					arr2.append(arr[i][ii+2])
				if ii>=2:
					# print(i, ii-2)
					arr2.append(arr[i][ii-2])
				for abc in range(1,6):
					if not(abc in arr2):
						final = abc
						if mxm<final:
							mxm=final
						break
				arr[i][ii] = final
			n+=1
		if m<mm:
			# print("''''''",m,mm)
			for i in range(n):
				ii = m
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
					# print(i+2,  ii)
					arr2.append(arr[i+2][ii])
				if ii<=m-3:
					arr2.append(arr[i][ii+2])
				if ii>=2:
					arr2.append(arr[i][ii-2])
				for abc in range(1,6):
					if not(abc in arr2):
						final = abc
						if mxm<final:
							mxm=final
						break
				arr[i][ii] = final
			m+=1
	return arr

def check_max_n(n,m):

	if n==1 and m==1:
		ans = 1
	elif (n==1 and m==2) or (n==2 and m==1):
		ans=1
	elif n==1 or m==1 or(n==2 and m==2):
		ans=2
	elif (n==2 or m==2):
		ans = 3
	else:
		ans=4
	return ans


arr50 = go(50,50)
for x in range(int(input())):

	n2,m2 = list(map(int, input().split()))


	if n2>3 and m2>3:

		print(4)
		# check_val(arr)
		# prt = True
		for i in range(n2):
			print (" ".join(str(arr50[i][v]) for v in range(m2)))
	
	else:
		print(check_max_n(n2,m2))

		arrf = go(n2,m2)

		for i in arrf:
			print(" ".join(str(v) for v in i))




		


# arr2.append(arr[i-1][ii+1])
# arr2.append(arr[i-1][ii-1])
# arr2.append(arr[i-2][ii])

# arr2.append(arr[i+1][ii+1])
# arr2.append(arr[i+1][ii-1])
# arr2.append(arr[i+2][ii])

# arr2.append(arr[i][ii+2])

# arr2.append(arr[i][ii-2])



				




