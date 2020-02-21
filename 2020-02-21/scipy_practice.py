import scipy
import scipy.stats


# Create a normal distributed random variable
X = scipy.stats.norm(1, 0.5)
# Draw a random sample from the distribution
print(X.rvs(10))
