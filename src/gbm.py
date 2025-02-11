import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def geo_brownian_paths(S, T, r, q, sigma, steps, N):
    '''
    S = Stock price
    T = time to maturity
    r = risk free
    q = dividend rate
    steps = time increments
    N = Number of trials

    returns:
    matrix of price paths
    '''

    dt = T/steps

    # ito integral
    ST = np.log(S) + np.cumsum(((r - q - sigma**2/2)*dt +\

    sigma*np.sqrt(dt) * \

    np.random.normal(size=(steps,N))),axis=0)

    return np.exp(ST)

def prob_over(value, S, T, r, q, sigma, steps, N, show_plot=True):
    '''
    value: value you want to check S_T is above p(value < S_T)
    '''
    paths = geo_brownian_paths(S,T, r, q, sigma, steps, N)
    ST = paths[-1]
    over = len(ST[ST>value])
    # print(f"probability of stock being above {value} is {round(over/len(ST)*100,3)}%")

    if show_plot:
        _ = plt.hist(paths[-1],bins=200)
        plt.axvline(value, color='black', linestyle='dashed', linewidth=2)
        plt.show()

    return over/len(ST)



def prob_under(value, S, T, r, q, sigma, steps, N, show_plot=True):
    '''
    value: this refers to the value you want to check p(S_T < value)
    returns: probability in %
    '''
    paths = geo_brownian_paths(S,T, r, q, sigma, steps, N)
    ST = paths[-1]
    under = len(ST[ST<value])
    
    # print(f"probability of stock being below {value} is {round(under/len(ST)*100,3)}%")

    if show_plot:
        _ = plt.hist(paths[-1],bins=200,color='blue')
        plt.axvline(value, color='black', linestyle='dashed', linewidth=2) 
        plt.show()   

    return under/len(ST)

# if __name__ == "__main__":
    
    # #example of geo brownian paths
    # paths = geo_brownian_paths(100, 1, 0.05, 0.02, 0.20, 100, 100)

    # #show distribution of final values
    # _ = plt.hist(paths[-1],bins=200)

    # #show geometric brownian paths
    # _ = plt.plot(paths)
    # plt.show()

    #example
    # S = 121 #price today
    # value = 116
    # T = 1 # one year , for one month 1/12, 2months = 2/12 etc
    # r = 0.01 # riskfree rate: https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/TextView.aspx?data=billrates
    # q = 0.007 # dividend rate
    # sigma = 0.4 # annualized volatility
    # steps = 1 # no need to have more than 1 for non-path dependent security
    # N = 1000000 # larger the better

    # # probability of over value
    # # Params: value, S, T, r, q, sigma, steps, N, 
    # # prob_over(value, S, T, r, q, sigma, steps, N, show_plot=True)

    # # #probability of less than value , Not showing hist
    # prob_under(value, S, T, r, q, sigma, steps, N, show_plot=True)