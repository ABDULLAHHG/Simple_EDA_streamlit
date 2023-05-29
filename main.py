import numpy as np 
import pandas as pd 
import streamlit as st 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
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

def subplot(df , column):

    # Color for Pie plot and Bar plot 
    colors = ['#a2b9bc', '#6b5b95', '#b2ad7f', '#feb236', '#b5e7a0', '#878f99',
              '#d64161', '#86af49', '#ff7b25']
    

    fig = make_subplots(rows=1, cols=2, subplot_titles=('Countplot', 'Bar'), specs=[[{"type": "xy"}, {'type': 'domain'}]])

    # Bar plot
    fig.add_trace(
        go.Bar(
            x=df[column].value_counts().index,
            y=df[column].value_counts().values,
            textposition='auto',
            showlegend=False,
            marker=dict(
                color=colors[:len(df[column].value_counts())],  
                line=dict(color='black', width=2)
            )
        ),
        row=1,
        col=1
    )

    # Pie plot 
    fig.add_trace(
        go.Pie(
            labels=df[column].value_counts().index,
            values=df[column].value_counts().values,
            hoverinfo='label',
            textinfo='percent',
            textposition='auto',
            marker=dict(
                colors=colors[:len(df[column].value_counts())],  
                line=dict(color='black', width=2)
            )
        ),
        row=1,
        col=2
    )

    fig.update_layout(
        title = {'text' : f'Distribution of the {column}',
                 'y' : 0.9,
                 'x' : 0.5,
                 'xanchor' : 'center',
                  'yanchor' : 'top'},
                  template = 'plotly_dark')
    st.plotly_chart(fig)
    

column = st.selectbox('Selecte column you want to compare with Income' , df.columns , 1 )
# st.text(columns_to_drop)
compare = df.groupby(column).sum()
columns_to_drop = [i for i in compare.columns if compare[i].dtype != 'float64']

compare = compare.drop(columns_to_drop , axis = 1 ).reset_index()
st.dataframe(compare)

plot(compare[column],compare['Income'])

subplot(df , column)
st.dataframe(df.Gender.value_counts())

