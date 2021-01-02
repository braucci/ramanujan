import math as m

def fatt(i):
	if i==0:
		return 1
	else:
		return i*fatt(i-1)

def pi_ramanujan():
	sum=0
	n=0
	number = (2*m.sqrt(2)) / 9801

	while True:
		num = fatt(4*n) * (1103 + 26390*n)
		den = (fatt(n)**4)*396**(4*n)
		sum1 = sum
		sum = sum + number * (num/den)

		if abs(sum-sum1) < 1e-15:
			break
		n = n + 1
	return 1/sum

print("Pi Greco Serie: ", pi_ramanujan())
print("Pi Greco Python: ", m.pi)  