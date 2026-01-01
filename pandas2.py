#Write a program to generate 1000 random samples from a normal distribution with mean 10 and SD 3.
#Then plot a histogram with these values
from scipy.stats import norm
import matplotlib.pyplot as plt
M=10
SD=3
samples = norm.rvs(M,SD,size=1000)
plt.hist(samples,bins=50)
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('Normal Distribution')
plt.show()

