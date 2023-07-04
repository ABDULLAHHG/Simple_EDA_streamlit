import numpy as np 
import pandas as pd 
import streamlit as st 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
import matplotlib.pyplot as plt 

# Load dataset
df = pd.read_csv('Credit Score Classification Dataset.csv')

# Color for Pie plot and Bar plot 
colors = ['#7c90db', '#92a8d1', '#a5c4e1', '#f7cac9', '#fcbad3', '#e05b6f', '#f8b195', '#f5b971', '#f9c74f', '#ee6c4d', '#c94c4c', '#589a8e', '#a381b5', '#f8961e', '#4f5d75', '#6b5b95', '#9b59b6', '#b5e7a0', '#a2b9bc', '#b2ad7f', '#679436', '#878f99', '#c7b8ea', '#6f9fd8', '#d64161', '#f3722c', '#f9a828', '#ff7b25', '#7f7f7f']
    

for i in df.columns:
    try :       
        df[i] = df[i].astype(float)
    except: 
        continue
df['Number of Children'] = df['Number of Children'].astype(int)

column = st.selectbox('Selecte column you want to compare with Income' ,[ i for i in df.columns if i != 'Income'], 1 )

# fucntion to plot barplot plotly 
def plot(x,y,column):
    
    fig = go.Figure(data =go.Bar(x = x , y = y,
    marker=dict(
                color=colors[:len(df[column].value_counts())],  
                line=dict(color='black', width=2)
            )))

    fig.update_layout(
        title = f'{x.name} VS {y.name}',
        xaxis_title = f'{x.name}',
        yaxis_title = f'{y.name}',
    )
    st.plotly_chart(fig)

def subplot(df , column):

    fig = make_subplots(rows=1, cols=2, subplot_titles=('Countplot', 'percentage'), specs=[[{"type": "xy"}, {'type': 'domain'}]])

    # Bar plot
    fig.add_trace(
        go.Bar(
            x=df[column].value_counts().index,
            y=df[column].value_counts().values,
            textposition='auto',
            showlegend=False,
            marker=dict(
                color=colors[:len(df[column].value_counts())],  
                line=dict(color='black', width=0)
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
    
def compare_columns_with_income(df):
    compare = df.groupby(column).sum()
    columns_to_drop = [i for i in compare.columns if compare[i].dtype != 'float64']
    compare = compare.drop(columns_to_drop , axis = 1 ).reset_index()
    a = [column,'Income']
    st.dataframe(compare[a])
    plot(compare[column],compare['Income'],column)
    subplot(df , column)
    st.dataframe(df[column].value_counts())


compare_columns_with_income(df)

# st.checkbox('choose feature',)
# mode = ['lines', 'markers', 'text']
# groupby_list = [column]

# def compare_2_columns_with_income(df):


#     trace1 = go.Bar(
#         x = df.Income,
#         y = df.Age,
#         mode = 'lines',
#         marker = dict(color = colors[3]),
#         text = df.Education 

#     )

#     # trace2 = go.Bar(
#     #     x = df.Income,
#     #     y = df['Number of Children'],
#     #     marker = dict(color =colors[5]),
#     #     text = df.Education)
    




# def compare_multi_column(df):
#     layout = dict(title = 'age and Number of Children vs Income', xaxis = dict(title = 'Income' , ticklen = 5))
#     list_to_plot = []
#     fig = dict(layout = layout)

#     for k , i in enumerate([ j for j in df.columns if j != 'Income' and j != column and df[j].dtype != 'float64' ]):
#         checkbox = st.checkbox(i)
#         if checkbox and len(groupby_list) < 5:
#             variable_name = f"{i}"
#             locals()[variable_name] = go.Bar(
#                 x = df[i],
#                 y = df.Income,
#                 name = f'{i}',
#                 marker = dict(color = colors[k],
#                               line = dict(color=colors[k] ,width = 1.5)))
#             list_to_plot.append(locals()[variable_name])
#             fig.update({'data' : list_to_plot  })

        

#     st.plotly_chart(fig)

#     st.text(groupby_list)


# # compare_2_columns_with_income(df)

# compare_multi_column(df)
