1. Febonacci Series::
 
def febo(num):
	a,b=0,1
	while(b<num):
		print a
		a,b=b,a+b
febo(10)


2. Series Of Prime Number::

def prime(num):
	for i in range(2,num+1):
		count=0
		for j in range(2,i):
			if(i%j !=0):
				count+=1
		if(count==i-2):
			print i

prime(20)
