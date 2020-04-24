import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.linear_model import LinearRegression
from scipy.stats import norm

# significance of point insight.
powerlaw = lambda i, a, b: a * (i ** b)
xdata = [ 3250, 5500, 10000, 32500, 55000, 77500, 100000, 200000]
ydata = [ 500, 288, 200, 113, 67, 52, 44, 5 ]
# yerr = 0.2 * ydata
# ydata += np.random.randn(100) * yerr

logx = np.log10(xdata)
logy = np.log10(ydata)

fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y:(fitfunc(p, x) - y)

pinit = [1.0, -1.0]
out = optimize.leastsq(errfunc, pinit, args=(logx, logy), full_output=1)

pfinal = out[0]
covar = out[1]
print(pfinal)
print(covar)

index = pfinal[1]
amp = 10.0**pfinal[0]
pred = powerlaw(1100, amp, index)

err_array = ydata - powerlaw(xdata, amp, index)
print("predicted value: ", pred)
print(err_array)
random_sample = norm.rvs(loc=0,scale=1,size=200)
parameters = norm.fit(random_sample)

print('p value:', norm(parameters[0], parameters[1]).pdf(2))
x = np.linspace(-5,5,100)

# Generate the pdf (fitted distribution)
fitted_pdf = norm.pdf(x,loc = parameters[0],scale = parameters[1])
normal_pdf = norm.pdf(x)

plt.plot(x,fitted_pdf,"red",label="Fitted normal dist",linestyle="dashed", linewidth=2)
plt.plot(x,normal_pdf,"blue",label="Normal dist", linewidth=2)
plt.hist(random_sample,normed=1,color="cyan",alpha=.3) #alpha, from 0 (transparent) to 1 (opaque)
plt.title("Normal distribution fitting")
# insert a legend in the plot (using label)
plt.legend()

# we finally show our work
plt.show()


indexErr = np.sqrt( covar[1][1] )
ampErr = np.sqrt( covar[0][0] ) * amp

# plt.clf()
# plt.subplot(2, 1, 1)
# plt.plot(xdata, powerlaw(xdata, amp, index))     # Fit
# plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
# plt.text(5, 6.5, 'Ampli = %5.2f +/- %5.2f' % (amp, ampErr))
# plt.text(5, 5.5, 'Index = %5.2f +/- %5.2f' % (index, indexErr))
# plt.title('Best Fit Power Law')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.xlim(0, )

# plt.figure(figsize=(10, 5))
# plt.plot(xdata, powerlaw(xdata, amp, index), '--')
# plt.plot(xdata, ydata, 'ro')
# plt.legend()
# plt.show()




# x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
# y = np.array([5, 20, 14,32, 22, 38])
#
# model = LinearRegression()
# model.fit(x, y)
#
# r2 = model.score(x, y)
# print('coefficient of determination:', r2)
#
# y_pred = model.predict(x)
# print('predicted response:', y_pred)


# Significance of shape insight


