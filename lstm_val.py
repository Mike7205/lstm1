# To jest wersja 2 nowej strony - gdzie modele mają opisy i parametry i jest ich więcej

import streamlit as st
from streamlit import set_page_config
import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime, timedelta, date
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import appdirs as ad
CACHE_DIR = ".cache"
# Force appdirs to say that the cache dir is .cache
ad.user_cache_dir = lambda *args: CACHE_DIR
# Create the cache dir if it doesn't exist
Path(CACHE_DIR).mkdir(exist_ok=True)


# Set page configuration for full width
set_page_config(layout="wide")
# Definicje
today = date.today()

st.title('Last 50 results of LSTM Model D+1 predictions')
st.divider()

st.subheader('USD/PLN exchange rate (D+1) predictions')
val_USD = pd.read_excel('LSTM_mv.xlsx', sheet_name='D1_USD')
val_USDD1 = val_USD[['Date','USD/PLN','Day + 1 Prediction']].iloc[:-1]

fig_USDD1 = px.line(val_USDD1[-50:], x='Date', y=['USD/PLN','Day + 1 Prediction'], color_discrete_map={
                  'USD/PLN': 'orange', 'Day + 1 Prediction': 'dodgerblue'}, width=1000, height=500) #'mediumseagreen'
fig_USDD1.update_layout(plot_bgcolor='white',showlegend=True,xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'),
                      yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'))

#fig_USDD1.add_vline(x = today,line_width=1, line_dash="dash", line_color="black")
fig_USDD1.update_layout(xaxis=None, yaxis=None)    
st.plotly_chart(fig_USDD1, use_container_width=True)  


st.subheader('EUR/PLN exchange rate (D+1) predictions')
val_EUR = pd.read_excel('LSTM_mv.xlsx', sheet_name='D1_EUR')
val_EURD1 = val_EUR[['Date','EUR/PLN','Day + 1 Prediction']].iloc[:-1]

fig_EURD1 = px.line(val_EURD1[-50:], x='Date', y=['EUR/PLN','Day + 1 Prediction'], color_discrete_map={
                  'EUR/PLN': 'deeppink', 'Day + 1 Prediction': 'dodgerblue'}, width=1000, height=500)
fig_EURD1.update_layout(plot_bgcolor='white',showlegend=True,xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'),
                      yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'))

#fig_EURD1.add_vline(x = today,line_width=1, line_dash="dash", line_color="black")
fig_EURD1.update_layout(xaxis=None, yaxis=None)    
st.plotly_chart(fig_EURD1, use_container_width=True) 

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"



sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")

#st.context.cookies
