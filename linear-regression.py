import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ডেটাসেট তৈরি করা
X = np.array([1000, 1500, 2000, 2500, 3000]).reshape(-1, 1)  # বাড়ির আয়তন
y = np.array([150, 200, 250, 300, 350])  # বাড়ির মূল্য

# লিনিয়ার রিগ্রেশন মডেল তৈরি করা
model = LinearRegression()
model.fit(X, y)

# ভবিষ্যদ্বাণী করা
predicted_price = model.predict(np.array([[2200]]))
print(f"2200 বর্গফুট বাড়ির অনুমানিক মূল্য: {predicted_price[0]:.2f} হাজার টাকা")

# ডেটা এবং রিগ্রেশন লাইন প্লট করা
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Home Size')
plt.ylabel('Home Price')
plt.title('Linear Regression')
plt.legend()
plt.show()