import math
from stock_volatility import stock_vol

class stockoption():

	def __init__(self, S0, K, r, T, N, prm):
		'''
		S0 = initial stock price
		K = strike price
		r = risk free interest rate per annum
		T = length of option in years
		N = number of binomial iterations
		prm = dictionary with additional parameters
		'''
		self.S0 = S0
		self.K = K
		self.r = r
		self.T = T
		self.N = N
		'''
		further parameters:
<<<<<<< HEAD
		start = date from when you want to analyse stocks
		end = date of final stock analysis (likely current date)
		tk = ticker label
		div = dividend paid
		is_cal = is volatility calculated using stock price history
=======

      tk = ticker label
      div = dividend paid
      is_cal = is volatility calculated using stock price history
>>>>>>> 229098793e7c98fe9f8abdc5e6b4c3e68256c675
		sigma = volatility of stock
		is_call = call or put option
		eu_option = European or American option
		'''
<<<<<<< HEAD
		self.tk = prm.get('tk', None)
		self.start = prm.get('start', None)
		self.end = prm.get('end', None)
		stock_vol.get_data(self.tk, self.start, self.end)
		self.div = prm.get('div', 0)
		if is_cal == True:
			stock_vol.exp_sigma()
			self.sigma = sigma
		else:
			self.sigma = prm.get('sigma', 0)
=======
      self.tk = prm.get('tk', 0)
		self.div = prm.get('div', 0)
      if is_cal == True:
        # calculate volatility using ewm
      else:
        self.sigma = prm.get('sigma', 0)
>>>>>>> 229098793e7c98fe9f8abdc5e6b4c3e68256c675
		self.is_call = prm.get('is_call', True)
		self.eu_option = prm.get('eu_option', True)
		'''
		derived values:
		dt = time per step, in years
		df = discount factor
		'''
		self.dt = T/float(N)
		self.df = math.exp(-(r-self.div)*self.dt)
