import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.linear_model import LinearRegression
from scipy.stats import norm
from scipy.stats import logistic
import collections
from sklearn.metrics import r2_score



def insight_score(result_set, type, total_tuples):
    # result_set is a dictionary
        #key: the subspace as a tuple
        #val: an array of measures in each level
    # type
        # 1 for point insight
        # 2 for shape insight
    # total_tuples: the total number of publications
    # R question number

    #calculate the impact measure
    imp = 0
    for val in result_set.values():
        imp += val[0] / total_tuples
    if type == 1:
        #  SIG of point insight
        return imp * sig_point(result_set)
    elif type == 2:
        # SIG of shape insight
        return imp * sig_shape(result_set)


def sig_point(result_set):
    # significance of point insight.
    # pull the last column from the dictionary values. Then sort the array.

    last_column = np.array(list(result_set.values()))[:, -1]
    lc_sort = np.sort(last_column)[::-1]
    # Y = lc_sort[1:]
    Y = np.trim_zeros(lc_sort[1:])
    if(len(Y) <= 1):
        return 0
    # Y = np.ma.masked_equal(lc_sort[1:], 0)
    X = np.arange(2, len(Y) + 2)
    Y_max = lc_sort[0]

    powerlaw = lambda i, a, b: a * (i ** b)
    # xdata = [ 3250, 5500, 10000, 32500, 55000, 77500, 100000, 200000]
    # ydata = [ 500, 288, 200, 113, 67, 52, 44, 5 ]
    # yerr = 0.2 * ydata
    # ydata += np.random.randn(100) * yerr

    logx = np.log10(X)
    logy = np.log10(Y)

    powerlawfunc = lambda p, x: p[0] + p[1] * x
    errfunc = lambda p, x, y:(powerlawfunc(p, x) - y)

    pinit = [1.0, -1.0]
    out = optimize.leastsq(errfunc, pinit, args=(logx, logy), full_output=1)

    pfinal = out[0]
    covar = out[1]
    # print(pfinal)
    # print(covar)

    index = pfinal[1]
    amp = 10.0**pfinal[0]

    pred = powerlaw(1, amp, index)

    err_array = Y - powerlaw(X, amp, index)
    # print("predicted value: ", pred)
    # random_sample = norm.rvs(loc=0,scale=1,size=200)
    parameters = norm.fit(err_array)
    p = 1 - norm(parameters[0], parameters[1]).cdf(pred - Y_max)
    # print('p value:', p)



    # x = np.linspace(-5,5,100)
    # # Generate the pdf (fitted distribution)
    # fitted_pdf = norm.pdf(x,loc = parameters[0],scale = parameters[1])
    # normal_pdf = norm.pdf(x)
    #
    # plt.plot(x,fitted_pdf,"red",label="Fitted normal dist",linestyle="dashed", linewidth=2)
    # plt.plot(x,normal_pdf,"blue",label="Normal dist", linewidth=2)
    # plt.hist(random_sample,normed=1,color="cyan",alpha=.3) #alpha, from 0 (transparent) to 1 (opaque)
    # plt.title("Normal distribution fitting")
    # # insert a legend in the plot (using label)
    # plt.legend()
    #
    # # we finally show our work
    # plt.show()


    # indexErr = np.sqrt( covar[1][1] )
    # ampErr = np.sqrt( covar[0][0] ) * amp

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
    if(p == None):
        return 0
    # print('type: ', type(1 - p))
    return float(1 - p)
# Significance of shape insight
def sig_shape(result_set):

    sorted_set = collections.OrderedDict(sorted(result_set.items(), key=lambda x: x[0][1]))
    year = np.array(list(sorted_set.keys()))[:, 1].reshape((-1, 1))
    last_column = np.array(list(sorted_set.values()))[:, -1]

    # x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    # y = np.array([5, 20, 14, 32, 22, 38])

    model = LinearRegression()
    model.fit(year, last_column)
    pred = model.predict(np.array(list(map(float,year))).reshape((-1, 1)))
    #r2 = model.score(np.array(list(map(float,last_column))).reshape((-1, 1)), np.array(list(map(float,last_column))).reshape((-1, 1)))
    r2 = r2_score(last_column, pred)
    slope = model.coef_
    # print('coefficient of determination:', r2)
    # print('intercept:', model.intercept_)
    # print('slope:', model.coef_)

    # y_pred = model.predict(x)
    # print('predicted response:', y_pred)
    p = 0
    if(slope > 0):
        p = (logistic(0.2, 2).cdf(-slope)) + 1 - (logistic(0.2, 2).cdf(slope))
    else:
        p = (logistic(0.2, 2).cdf(slope)) + 1 - (logistic(0.2, 2).cdf(-slope))
    # print('p value:', p)
    # print('return val: ', type(r2*(1 - p)))
    return float(r2*(1 - p))