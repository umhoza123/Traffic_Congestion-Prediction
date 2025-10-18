import pickle
import numpy as np
import streamlit as st
with open(r'ving.pkl', 'rb') as f:
    model=pickle.load(f)
st.title("traffic congestion")
st.write("fill the following information") 
week=st.selectbox("Day of week",['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
CarCount=st.number_input("CarCount")
BikeCount=st.number_input("BikeCount")
BusCount=st.number_input("BusCount")
Total=st.number_input("Total")
days=0
if week=='Mon':
    days=1
if week=='Tue':
    days=2
if week=='wed':
    days=3
if week=='Thur':
    days=4
if week=='fri':
    days=5
if week=='sat':
    days=6
if week=='sun':
    days=7

if st.button("predict"):
    data=np.array([[CarCount,BikeCount,BusCount,Total,days]])
    pred=model.predict(data)
    st.success(f"traffic congestion:{pred[0]}")

