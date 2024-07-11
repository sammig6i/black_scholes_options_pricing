import numpy as np
from scipy.stats import norm


#TODO variables: volatility (sigma), price of underlying asset (S), strike price (K), time until maturity (T), risk-free interest rate (r), and type of option (call or put)

class BlackScholesModel:
  def __init__(self, S, K, T, r, sigma):
    self.S = S # price of underlying
    self.K = K # strike price
    self.T = T # Time to maturity in years
    self.r = r # risk-free interest rate
    self.sigma = sigma

  def calculate_d1_d2(self):
    d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
    d2 = d1 - (self.sigma * np.sqrt(self.T))

    return d1, d2
  
  def calculate_call_price(self):
    d1, d2 = self.calculate_d1_d2()
    call_price = self.S * self.norm_cdf(d1) - self.K * np.exp(-self.r * self.T) * self.norm_cdf(d2)
    return call_price

  def calculate_put_price(self):
    d1, d2 = self.calculate_d1_d2()
    put_price = self.K * np.exp(-self.r * self.T) * self.norm_cdf(-d2) - self.S * self.norm_cdf(-d1)
    return put_price

  def norm_cdf(self, x):
    return norm.cdf(x)

