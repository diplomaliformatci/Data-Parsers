import pandas as pd

data = {'user_id':[1,2,3,4] , 'age' : [25,23,5,2]}
frame = pd.DataFrame(data,columns=['user_id','age'])
print(frame.head())

frame['over_thirty'] = frame['age'] > 30

print(frame.head())

frame['likes_python'] = pd.Series([True,False,True,True], index = frame.index)

print(frame.head())

print(frame.describe())