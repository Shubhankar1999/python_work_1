from operator import itemgetter
import bisect
# def binary_search(a, x, lo=0, hi=None):
#     if hi is None:
#         hi = len(a)
#     while lo < hi:
#         mid = (lo+hi)//2
#         midval = a[mid]
#         if midval < x:
#             lo = mid+1
#         elif midval > x: 
#             hi = mid
#         else:
#             return mid
#     return -1
N, M =  list(map(int, input().split()))
# print(N,"and", M)
al =  list(map(int, input().split()))
bl =  list(map(int, input().split()))


al2 = []
bl2 = []
for i in range(N):
	al2.append([i, al[i]])
for i in range(M):
	bl2.append([i, bl[i]])

al2 = sorted(al2, key=itemgetter(1))
bl2 = sorted(bl2, key=itemgetter(1))


# print(al2, "\n", bl2)
	

for i in range(M):
	print(al2[0][0], bl2[i][0])

for i in range(1,N):
	print(al2[i][0], bl2[M-1][0])


# al2 = []
# bl2 = []
# for i in range(N):
# 	al2.append([i, al[i]])
# for i in range(M):
# 	bl2.append([i, bl[i]])
# print("\n---------------------\n",al2,"\n........................\n",bl2)
# al2 = sorted(al2, key=itemgetter(1))
# bl2 = sorted(bl2, key=itemgetter(1))

# print("\n---------------------\n",al2,"\n........................\n",bl2)
# pta = 0
# ptb = 0
# for i in range(N+M-1):

# 	print(al2[pta][0], bl2[ptb][0])

# 	present = al2[pta][1] + bl2[ptb][1]

# 	while pta<N or ptb<M:

# 		if ( pta<N-1 and ptb<M-1 and al2[pta+1][1] + bl2[ptb][1] <= al2[pta][1] + bl2[ptb+1][1]) or ptb>= M-1:

# 			pta+=1
# 			print("A inc.")

# 			if al2[pta][1] + bl2[ptb][1] != present:
# 				break
# 		elif ( ptb<M-1 and pta<N-1 and al2[pta+1][1] + bl2[ptb][1] > al2[pta][1] + bl2[ptb+1][1] ) or pta>= N-1:

# 			ptb+=1
# 			print("B inc.")

# 			if al2[pta][1] + bl2[ptb][1] != present:
# 				break




