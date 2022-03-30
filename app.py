import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import helpers as hp
st.set_page_config(layout = "wide")
st.title('Statistic Optics Example')
st.header("Binomialverteilung")
st.write("Dieses Dashboard simuliert eine Binomialverteilung, wie sie z.B. an den Ausgängen eines n-stufigen Galtonbrettes beobachtet werden kann.")
st.write("Stelle zunächst ein, bis zu welcher Stufe das Galtonbrett simuliert werden soll:")


input = st.number_input("Stufe des Galtonbretts:", 0, 100,1, key = "anzahl")

c1, c2, c3 = st.columns([1,1,1])

if 'count' not in st.session_state:
    st.session_state.count = 0
if "anzahl" not in st.session_state:
    st.session_state.anzahl = input
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(np.zeros(st.session_state.anzahl+1), 
                            index = [n+1 for n in range(st.session_state.anzahl+1)])
if "results" in st.session_state and len(st.session_state.results) -1 != st.session_state.anzahl:
    st.session_state.results = pd.DataFrame(np.zeros(st.session_state.anzahl+1), 
                            index = [n+1 for n in range(st.session_state.anzahl+1)])
    st.session_state.count = 0
    st.write("Anzahl geändert")


st.write(f"Stufe des Galtonbretts: {st.session_state.anzahl}")


def increment_counter(n:int):
    spacings = hp.spacings(st.session_state.anzahl)
    for i in range(n):
        rand_num = np.random.rand()
        #st.write(rand_num)
        for k in range(len(spacings)-1):
            if rand_num >= spacings[k] and rand_num <= spacings[k+1]:
                st.session_state.results.loc[k+1] += 1
                st.session_state.results.loc[k+1] = int(st.session_state.results.loc[k+1])
                #st.write(str(k+1))
    with c3:
        st.dataframe(st.session_state.results)
    
with c1:
    st.empty()
    st.write("Klicke nun auf die Buttons, um die Kugeln rollen zu lassen!")
    incr1 = st.button('1 Kugel')
    incr10 = st.button('10 Kugeln')
    incr100 = st.button('100 Kugeln')
    if incr1:
        increment_counter(1)
        st.session_state.count += 1
    if incr10:
        increment_counter(10)
        st.session_state.count += 10
    if incr100:
        increment_counter(100)
        st.session_state.count += 100

    st.write("Counts: ", st.session_state.count)

with c2:
    fig = px.bar(st.session_state.results,  height=400)
    st.plotly_chart(fig)





