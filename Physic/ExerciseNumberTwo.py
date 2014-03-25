import matplotlib
matplotlib.use('Agg')
import math,matplotlib.pyplot as plt,pandas
#Setting Graph
def setPlot(x,y,name):
	x = sorted(x)
	y = sorted(y)
	plt.grid(True)
	plt.plot(x,y,'ro',x,y)
	plt.savefig('/home/stevan/Dropbox/'+name+'.png')


gbg = 9.8060226
#First Part
try:
	print '****PRVI DEO****\n\nUneti vrednosti za l1,l2,tu,n:'
	values = [raw_input().split(" ") for i in range(5)]
	ls = [(float(data[0])+float(data[1]))/2 for data in values]
	ls2 = [data**2 for data in ls]
	T = [float(data[2])/float(data[3]) for data in values]
	T2 = [data**2 for data in T]
	a = sum(T2[i]*ls[i] for i in range(5))/sum(ls2)
	g = (4*math.pi**2)/a
	Er = (abs(g-gbg)/gbg)*100
	data = [ls,ls2,T,T2]
	print
	print  pandas.DataFrame(data,['ls','ls^2','T','T^2'],['1','2','3','4','5'])
	print "\na = {} \ng= {} \nEr = {}".format(str(round(a,7)),str(round(g,7,)),str(round(Er,7)))
	try:
		#draw Graph
		setPlot(T2,ls,'T(ls)')
	except:
		print "Neuspesno crtanje grafika"
except:
	print 'Preskoci prvi deo'
plt.clf()
#Second Part
print '\n\n*****DRUGI DEO*****\n\n'
l = input("Unesite duzinu zice:")
d = [input("Precnik zice" + str(i) + ": ") for i in range(5)]
ds = sum(d)/5
print "ds : ",ds 
n = input("Unesite broj merenja:")
print "Unesite vrednosti redom : masa tega,pri povecanju sile,pri smanjenju sile"
values = [raw_input().split(" ") for i in range(n)]
m = [float(data[0]) for data in values]
deltaL = [(float(data[1])+float(data[2]))/2 for data in values]
print "deltaL : " + " ".join(str(data) for data in deltaL)
m2 = [data**2 for data in m]
a = sum(m[i]*deltaL[i] for i in range(n))/sum(m2)
Ey = (4*gbg*l)/(math.pi*ds**2*a)
print "a= {}\nEy= {}".format(a,Ey)
u1 = (0.289)/1000
ud = 28.9/10000000
ua = math.sqrt(sum((deltaL[i] - a*m[i])**2 for i in range(n))/(n-2))
ua *= math.sqrt(n/(n*sum(m2) - (sum(m))**2))
merna_nes = math.sqrt((u1/2)**2 + ((2*ud)/ds)**2 + (ua/a)**2)
print "\nul = {}\nud = {}\nua = {}\nMerna nesigurnost = {}".format(u1,ud,ua,merna_nes)
try:
	#draw second Graph
	setPlot(deltaL,m,'l(m)')
except:
	print "Neuspesno crtanje grafika2"
