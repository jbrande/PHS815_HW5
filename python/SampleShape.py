import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

sys.path.append(".")
from python.Random import Random

# Find the area common to two intersecting circles: (x-0.5)^2 + y^2 = 1 and (x+0.5)^2 _ y^2 = 1

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

	# in this case, X and Y both range in [-1, 1]
	for i in range(0,Nsample):
		X = 2*random.rand() - 1
		Y = 2*random.rand() - 1

		nTotal += 1
		if(((X-0.5)**2 + Y*Y <= 1) and ((X+0.5)**2 + Y*Y <= 1)): #accept if inside both circles
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



	# calculate actual area of intersection area of two circles: https://mathworld.wolfram.com/Circle-CircleIntersection.html
	def halflens(r, d):
		return (r**2)*np.arccos(d/r)-d*np.sqrt((r**2) - (d**2))

	d = 1
	r = 1
	R = 1
	d1 = 0.5
	d2 = 0.5

	intersection = (halflens(R, d1) + halflens(r, d2))/4

	#plot calculated pi vs sample number
	fig1 = plt.figure()
	plt.plot(isample,calcInt)
	plt.ylabel(r'Approximate integral')
	plt.xlabel("Sample number")
	plt.xlim(0,isample[len(isample)-1])
	ax = plt.gca()
	ax.axhline(y=intersection,color='green',label=r'true value $\sim${:.3f}'.format(intersection))
	plt.title(r'Intersection between two circles as a function of number of samples')
	plt.legend()
	fig1.savefig("calcCirc.jpg", dpi=180)


	#plot accept/reject points
	fig2 = plt.figure(figsize=(8,8))
	ax2 = fig2.gca()
	ax2.set_aspect("equal")
	plt.plot(Xaccept,Yaccept,marker='o',linestyle='',color='green',label='accept')
	plt.plot(Xreject,Yreject,marker='o',linestyle='',color='red',label='reject')
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.legend()

	# plot the two intersecting circles
	ax2.add_patch(Circle((-0.5, 0), 1, ls='--', lw=2.5, ec="k", fc=None, fill=False, zorder=10))
	ax2.add_patch(Circle((0.5, 0), 1, ls="-.", lw=2.5, ec="k", fc=None, fill=False, zorder=10))
	ax2.set_xlim(-1, 1)
	ax2.set_ylim(-1, 1)
	plt.title(r'Intersection of Two Circles: $(x+0.5)^2 + y^2 = 1$, $(x-0.5)^2 + y^2 = 1$')
	fig2.savefig("plotCirc.jpg", dpi=180)











