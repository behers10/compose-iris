# Docker Demo/Assignment

https://github.com/PGCSEDS-IIITH/compose-iris contains code which demonstrates docker and docker-compose using the IRIS dataset (https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)


## Pre-requisites
- Install `docker`
- Install `docker-compose`

## Running Instructions
- Create a fork of the repo using the `fork` button.
- Clone your fork using `git clone https://www.github.com/<your-username>/compose-iris.git`
- Build the images using `docker-compose build`
- Spin up the containers using `docker-compose up`

## Assignment Task
- Used Dibetes Data Set to do the task 
df=pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv',header=None)
df.columns=['no_times_pregant','glu_conc','bp','skin_thickness','insulin','mass_index','diabetes_pedgree','age','dibetes_yn']
X= df.loc[ : , df.columns != 'dibetes_yn']
y=df['dibetes_yn']
clf=GaussianNB()
clf.fit(X, y)
import pickle
pickle.dump(clf, open("pima_indians_diabetes.pkl", "wb"))

## Submission
Submit a link to your forked repository
