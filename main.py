import numpy as np 
import pandas as pd 
import streamlit as st 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 

# Load dataset
df = pd.read_csv('Credit Score Classification Dataset.csv')

for i in df.columns:
    try :       
        df[i] = df[i].astype(float)
    except:
        continue

# fucntion to plot barplot plotly 
def plot(x,y):
    fig = go.Figure(data =go.Bar(x = x , y = y))

    fig.update_layout(
        title = f'{x.name} VS {y.name}',
        xaxis_title = f'{x.name}',
        yaxis_title = f'{y.name}',
    )
    st.plotly_chart(fig)

column = st.selectbox('Selecte column you want to compare with Income' , df.columns , 1 )
# st.text(columns_to_drop)
compare = df.groupby(column).sum()
columns_to_drop = [i for i in compare.columns if compare[i].dtype != 'float64']

compare = compare.drop(columns_to_drop , axis = 1 ).reset_index()
st.dataframe(compare)

plot(compare[column],compare['Income'])



