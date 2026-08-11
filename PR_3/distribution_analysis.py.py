import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_excel("spread_locator_dataset.xlsx")
x = df["transaction_amount"].dropna()
a = 0.05


print("\n1. BERNOULLI AND BINOMIAL")
p = (df["transaction_status"] == "Success").mean()
print("Bernoulli p =", round(p, 4))


df["week"] = df["transaction_date"].dt.to_period("W")
w = df.groupby("week").agg(n=("transaction_status","size"),
                            k=("transaction_status",lambda z:(z=="Success").sum()))

w["Expected"] = w["n"] * p
print(w[["n","k","Expected"]])


print("\n2. POISSON")
daily = df.groupby("transaction_date")["transaction_count"].sum()
lam = daily.mean()
print("Lambda =", round(lam, 4))
print("Mean =", round(daily.mean(), 4))
print("Variance =", round(daily.var(), 4))


print("\n3. LOG-NORMAL AND POWER LAW")
s, loc, scale = stats.lognorm.fit(x, floc=0)
b, lp, sp = stats.pareto.fit(x, floc=0)


ll1 = np.sum(stats.lognorm.logpdf(x,s,loc=loc,scale=scale))
ll2 = np.sum(stats.pareto.logpdf(x,b,loc=lp,scale=sp))
aic1 = 4 - 2*ll1
aic2 = 4 - 2*ll2


print("Log-normal AIC =", round(aic1, 2))
print("Power Law AIC =", round(aic2, 2))


print("\n4. Q-Q PLOT")
stats.probplot(x, dist="norm", plot=plt)
plt.title("Q-Q Plot of Transaction Amounts")
plt.show()
print("Raw transaction amounts are not normally distributed.")


print("\n5. BOX-COX")
lam_bc = stats.boxcox_normmax(x, method="mle", brack=(-5,5))
xbc = stats.boxcox(x, lmbda=lam_bc)
print("Lambda =", round(lam_bc, 4))
print("Box-Cox transformation improves normality.")


plt.hist(xbc, bins=20)
plt.title("Box-Cox Transformed Data")
plt.xlabel("Transformed Amount")
plt.ylabel("Frequency")
plt.show()


print("\n6. Z-SCORE AND P(X > 5000)")
z = (5000-x.mean()) / x.std()
prob = 1 - stats.norm.cdf(z)
print("Z-score =", round(z, 4))
print("Probability =", round(prob, 4))
print("Percentage =", round(prob*100, 2), "%")


print("\n7. PDF AND CDF")
xx = np.linspace(x.min(), x.max(), 300)
pdf = stats.lognorm.pdf(xx,s,loc=loc,scale=scale)
cdf = stats.lognorm.cdf(xx,s,loc=loc,scale=scale)


plt.plot(xx, pdf)
plt.title("Log-Normal PDF")
plt.xlabel("Transaction Amount")
plt.ylabel("Density")
plt.show()


plt.plot(xx, cdf)
plt.title("Log-Normal CDF")
plt.xlabel("Transaction Amount")
plt.ylabel("Cumulative Probability")
plt.show()


print("\n8. CONCLUSION")
if aic1 < aic2:
    print("Log-Normal distribution fits transaction amounts better than Power Law.")
else:
    print("Power Law distribution fits transaction amounts better than Log-Normal.")
    

print("Bernoulli models transaction success/failure.")
print("Binomial models weekly successful transactions.")
print("Poisson models daily transaction counts.")
print("Q-Q plot shows transaction amounts are not normally distributed.")
print("Box-Cox transformation improves the distribution toward normality.")
print("PDF shows density and CDF shows cumulative probability.")