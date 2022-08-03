from nxfvars import nxfvars
import pandas as pd
import seaborn as sns

iris_path = nxfvars.get("iris_path", "../data/iris.csv")
# implicit variables - always available through nxfvars unless explicitly disabled
artifact_dir = nxfvars.get("artifact_dir", "/tmp")
cpus = nxfvars.get("cpus", 1)

iris = pd.read_csv(iris_path)

iris

ax = sns.scatterplot(x="sepal.width", y="petal.length", hue="variety", data=iris)

ax.get_figure().savefig(f"{artifact_dir}/plot.pdf", bbox_inches="tight")
