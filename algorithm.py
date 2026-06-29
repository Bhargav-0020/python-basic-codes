from sklearn.tree import DecisionTreeClassifier
x=[[20,25],[30,35],[40,45],[50,55]]
y=[0,0,1,1]
model=DecisionTreeClassifier()
model.fit(x,y)
prediction=model.predict([[25,30]])
print(prediction)