
for x in range(int(input())):

	n,p = list(map(int, input().split()))
	if n==1 and p==1:
		print(1)
		continue

	if n%2==0:
		no_g_n_by2m1 = p - (n//2 - 1)
	else:
		no_g_n_by2m1 = p - (n//2)

	no_g_n = p-n

	ans = (no_g_n_by2m1**2) + (no_g_n_by2m1*no_g_n) + (no_g_n**2)

	if (    ( (n%(n//2+1))%n)  %n ) == 0:
		print(p**3)

	else:
		print(ans)

