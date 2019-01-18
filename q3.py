for i in range(int(input())):

	N, a, b = list(map(int, input().split()))

	l1 = list(map(int, input().split()))
	ca = 0
	cb = 0
	w=0
	aliceWins = False
	for x in range(N):
		if l1[x]%a==0:       # WHEN BOB WINS
			ca+=1
		if l1[x]%b==0:
			cb+=1

		if l1[x]%b==0 and l1[x]%a==0:
			w += 1
	if w==0:
		if ca<=cb:
			aliceWins = True
	else:
		if cb> ca:
			aliceWins = True
	if aliceWins:
		print("ALICE")
	else:
		print("BOB")





