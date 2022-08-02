from nxfvars import nxfvars
import pandas as pd
import seaborn as sns

iris_path = nxfvars.get("iris_path", "../data/iris.csv")

iris = pd.read_csv(iris_path)

iris

sns.scatterplot(x="sepal.width", y="petal.length", hue="variety", data=iris)


