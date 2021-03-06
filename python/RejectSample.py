import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append(".")
from python.Random import Random

# Integrate under the curve sin(pi*x) from 0 to 1

if __name__ == "__main__":

	#set default number of samples
	Nsample = 1000

	# read the user-provided seed from the command line (if there)
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s -Nsample [number]" % sys.argv[0])
		print
		sys.exit(1) 

	nAccept = 0
	nTotal = 0
	
	# accepted values
	Xaccept = []
	Yaccept = []

	# reject values
	Xreject = []
	Yreject = []

	# sample number
	isample = []
	# calculated values of the integral
	calcInt = []

	random = Random()

	idraw = max(1,int(Nsample)/100000)
	print(idraw)
	for i in range(0,Nsample):
		X = random.rand()
		Y = random.rand()

		nTotal += 1
		if(Y < np.sin(np.pi*X)):#(X*X + Y*Y <= 1): #accept if inside
			nAccept += 1
			if(i % idraw == 0):
				Xaccept.append(X)
				Yaccept.append(Y)
		else: # reject if outside
			if(i % idraw == 0):
				Xreject.append(X)
				Yreject.append(Y)
		if(i % idraw == 0):
			isample.append(nTotal)
			calcInt.append(nAccept/nTotal)



	#plot calculated pi vs sample number
	fig1 = plt.figure()
	plt.plot(isample,calcInt)
	plt.ylabel(r'Approximate integral')
	plt.xlabel("Sample number")
	plt.xlim(0,isample[len(isample)-1])
	ax = plt.gca()
	ax.axhline(y=0.63662,color='green',label=r'true integral $\sim 0.63662$')
	plt.title(r'Approximation of $\int_0^1 \! sin(\pi x) \mathrm{d}x$ as a function of number of samples')
	plt.legend()

	fig1.savefig("calcInt.jpg", dpi=180)


	#plot accept/reject points
	fig2 = plt.figure()
	plt.plot(Xaccept,Yaccept,marker='o',linestyle='',color='green',label='accept')
	plt.plot(Xreject,Yreject,marker='o',linestyle='',color='red',label='reject')
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.legend()


	x_fn = np.arange(min(min(Xaccept),min(Xreject)),max(max(Xaccept),max(Xreject)),0.001)
	y_fn = np.sin(np.pi*x_fn)#[np.sqrt(1-i*i) for i in x_fn]
	plt.plot(x_fn,y_fn,color='blue',label=r'$sin(\pi * x)$')
	plt.legend()
	plt.title('Sampled points')
	fig2.savefig("plotInt.jpg", dpi=180)











