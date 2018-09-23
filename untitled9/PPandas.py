import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {
    'Day' : [1,2,3,4,5,6],
    'Visitors' : [32,1,56,6,7,2],
    'Bounce_Rate' : [43,43,6,56,1,3]
}

df = pd.DataFrame(web_stats)
print(type(df))
print(df)

print(df[['Visitors' , 'Day']])