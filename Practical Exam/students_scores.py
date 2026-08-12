import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis, probplot


df = pd.read_csv("student_scores_5000(1).csv")


print("Mean:", df["Math"].mean())
print("Median:", df["Math"].median())
print("Mode:", df["Math"].mode()[0])


print("Range:", df["Science"].max() - df["Science"].min())
print("Variance:", df["Science"].var())
print("Standard Deviation:", df["Science"].std())


print("Probability of Pass:", (df["Result"] == "Pass").mean())


df["Hours_Studied"] = df["Total"] / 50 > 5
print(pd.crosstab(df["Result"], df["Hours_Studied"]))


x = df[df["Hours_Studied"]]["Result"]
print("P(Pass | Hours_Studied > 5):", (x == "Pass").mean())


plt.hist(df["Math"], bins=15, density=True)
x = np.linspace(df["Math"].min(), df["Math"].max(), 100)
plt.plot(x, norm.pdf(x, df["Math"].mean(), df["Math"].std()))
plt.xlabel("Math Score")
plt.ylabel("Density")
plt.show()


print("Skewness:", skew(df["Science"]))
print("Kurtosis:", kurtosis(df["Science"]))


probplot(df["English"], dist="norm", plot=plt)
plt.show()


m = df["Math"].head(5).values
s = df["Science"].head(5).values


print("Math Vector:", m)
print("Science Vector:", s)
print("Dot Product:", np.dot(m, s))
print("Norm 1:", np.linalg.norm(m, 1))
print("Norm 2:", np.linalg.norm(m, 2))
print("Angle:", np.degrees(np.arccos(np.dot(m, s) / (np.linalg.norm(m) * np.linalg.norm(s)))))
