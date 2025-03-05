import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ডেটা লোড করুন
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# ফিচার ইঞ্জিনিয়ারিং
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = data[['Survived', 'Sex', 'Age', 'Fare', 'Pclass']].dropna()

X = data.drop('Survived', axis=1)
y = data['Survived']

# ট্রেইন-টেস্ট স্প্লিট
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# মডেল ট্রেইন (Gini ইম্পিউরিটি ব্যবহার করে)
clf = DecisionTreeClassifier(criterion='gini', max_depth=3)
clf.fit(X_train, y_train)

# ভিজুয়ালাইজেশন
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['Died', 'Survived'], filled=True)
plt.show()