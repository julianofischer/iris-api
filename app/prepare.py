from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target_names[iris.target])

from joblib import dump, load
dump(clf, 'iris_classifier.joblib')