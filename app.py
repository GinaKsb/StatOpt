import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd


#fig = px.histogram(df, x="total_bill")
#fig.show()

if 'count' not in st.session_state:
	st.session_state.count = 0

text='<p style="font-family:sans-serif; color:#565656; font-size: 42px;">Dashboard zur statistischen Optik</p>'
st.markdown(text, unsafe_allow_html=True)
st.text("Galtonbrett-Simulation für n Stufen:")

stufe = st.slider("Wie viele Stufen sollen simuliert werden?", 1, 30, 2) 
#st.write("Es werden", stufe, " Stufen simuliert.")


anzahl = 6
#results = {n+1 : 0 for n in range(anzahl)}
results = pd.DataFrame(np.zeros(anzahl), index = [n+1 for n in range(anzahl)])


dice = st.button("Einmal würfeln")
if dice:
    n = np.random.randint(1,7)
    results.loc[n] += 1
    st.session_state.count += 1
    
st.dataframe(results)
print(results)