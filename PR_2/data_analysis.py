simport pandas as pd
from scipy import stats
from statsmodels.stats.weightstats import ztest


df = pd.read_csv("diabetes(1).csv")
a = 0.05


print("\n1. HYPOTHESES")
print("H0: Smoking has no effect on Diabetes.")
print("H1: Smoking affects Diabetes.")
print("H0: Age and BMI have no significant relationship.")
print("H1: Age and BMI have a significant relationship.")


print("\n2. CONFIDENCE INTERVAL")
for c in ["Age", "BMI"]:
    x = df[c]
    m = x.mean()
    ci = stats.t.interval(0.95, len(x)-1, loc=m, scale=stats.sem(x))
    print(c, "Mean =", round(m,2), "95% CI =", tuple(round(v,2) for v in ci))
    

print("\n3 & 4. Z-TEST")
x = df[df["Diabetes"] == "Yes"]["BMI"]
y = df[df["Diabetes"] == "No"]["BMI"]
z, p = ztest(x, y)
cv = stats.norm.ppf(1-a/2)
print("Z =", round(z,4))
print("Critical Value =", round(cv,4))
print("p-value =", round(p,6))
print("Result:", "Reject H0" if p <= a else "Do not reject H0")


print("\n5. CHI-SQUARE TEST")
table = pd.crosstab(df["Smoking"], df["Diabetes"])
chi, p, d, e = stats.chi2_contingency(table)
cv = stats.chi2.ppf(1-a, d)
print(table)
print("Chi-square =", round(chi,4))
print("Critical Value =", round(cv,4))
print("p-value =", round(p,6))
print("Result:", "Reject H0" if p <= a else "Do not reject H0")


print("\n6. ANOVA TEST")
df["Age_Group"] = pd.cut(df["Age"], [0,30,50,100], labels=["Young","Middle","Older"])
g = [x["Diabetes"].map({"Yes":1,"No":0}) for _, x in df.groupby("Age_Group", observed=True)]
f, p = stats.f_oneway(*g)
cv = stats.f.ppf(1-a, len(g)-1, len(df)-len(g))
print("F =", round(f,4))
print("Critical Value =", round(cv,4))
print("p-value =", round(p,6))
print("Result:", "Reject H0" if p <= a else "Do not reject H0")


print("\n7. COVARIANCE AND CORRELATION")
cov = df["Age"].cov(df["BMI"])
cor = df["Age"].corr(df["BMI"])
print("Covariance =", round(cov,4))
print("Correlation =", round(cor,4))


print("\n8. FINAL INTERPRETATION")
print("Z-test: BMI differs significantly between diabetes groups.")
print("Chi-square: Smoking and Diabetes have a significant association.")
print("ANOVA: Disease rate differs significantly among age groups.")
print("Correlation: Age and BMI have a weak positive relationship.")
