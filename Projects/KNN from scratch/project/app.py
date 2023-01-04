import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

scaler = load(open('models/standard_scaler.pkl', 'rb'))
knn_classifier = load(open('models/knn_model.pkl', 'rb'))

st.title('Diamond Price Prediction')

#cut = st.text_input('cut')
#color = st.text_input('color')
#clarity = st.text_input('clarity')
x = st.number_input('x')
y = st.number_input('y')
z = st.number_input('z')
carat = st.number_input('carat')
depth = st.number_input('depth')
table = st.number_input('table')

#inp = [cut, color, clarity, x, y, z, carat, depth, table]
#df = pd.DataFrame(inp).T
#df.columns = ['cut', 'color','clarity', 'x','y', 'z', 'carat', 'depth', 'table']

inp = [x, y, z, carat, depth, table]
df = pd.DataFrame(inp).T
df.columns = ['x','y', 'z', 'carat', 'depth', 'table']

# --------------------------- cat ---------------------------------------------------
#df_cat = df.select_dtypes(include=['object'])

#cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
#color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}
#clarity_encoder = {'I1':1, 'SI2':2, 'SI1':3, 'VS2':4, 'VS1':5, 'VVS2':6, 'VVS1':7, 'IF':8}

#df_cat_le['cut'] = df_cat['cut'].apply(lambda x : cut_encoder[x])
#df_cat_le['color'] = df_cat['color'].apply(lambda x : color_encoder[x])
#df_cat_le['clarity'] = df_cat['clarity'].apply(lambda x : clarity_encoder[x])
# ------------------------------------------------------------------------------------------

# ------------------- numerical ------------------------------------------------------------


df_num = df.select_dtypes(include=['int64', 'float64'])

df_num_rescaled = pd.DataFrame(scaler.transform(df_num),
                                   columns = df_num.columns,
                                   index = df_num.index)
#-----------------------------------------------------------------------------------------

#df_transformed = pd.concat([df_num_rescaled, df_cat_le], axis=1)


button_click = st.button('predict')
if button_click == True:
    st.dataframe(df_num_rescaled.head())
#    prediction = knn_classifier.predict(df_transformed)
#    st.title(prediction)
