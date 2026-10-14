import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Hours studied (X) and exam scores (Y)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # predictor
Y = np.array([50, 55, 65, 70, 75, 85])           # outcome

model = LinearRegression()
model.fit(X, Y)

#Get slope and intercept
print("Slope (b1):", model.coef_[0])
print("Intercept (b0):", model.intercept_)

predicted = model.predict(X)

plt.scatter(X, Y, color="blue", label="Actual data")
plt.plot(X, predicted, color="red", label="Regression line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.show()
