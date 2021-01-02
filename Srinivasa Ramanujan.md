Il talento di **Srinivasa Ramanujan** ha suggerito diverse formule per il calcolo di <img src="https://render.githubusercontent.com/render/math?math=\pi">. Tra queste, valuteremo la bontà dei risultati ottenuti dalla seguente:
	
<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{\pi}=\frac{2\sqrt{2}}{9801}\sum_{n=0}^\infty\frac{(4n)!(1103+26390n)}{(n!)^4396^{4n}}">

Qui lo script Python per valutare <img src="https://render.githubusercontent.com/render/math?math=\pi"> attraverso la relazione precedente:

```
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
```

