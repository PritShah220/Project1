import  streamlit as st
import pandas as pd 

st.title("Student Info Form") 
name = st.text_input("Enter Name :")
course = st.selectbox("Enter Course:",("BCA","BBA","B.TEch","B.Com")) 
rno = st.selectbox("Enter Roll No:",(111,112,113,114,115,116,117,118,119,120))  
div = st.selectbox("Enter divison:",("A","B")) 
mname = st.text_input("Enter Mother Name") 
fname = st.text_input("Enter Father Name")
adr =st.text_input("Enter Email")
living = st.selectbox("Enter Living:",("Sojitra,Anand","Anand,Sojitra","Karamsad,Anand"))    
classdata = st.selectbox("Enter Your Class/College  :",(1,2,3,4,5,"College"))   

button = st.button("Submit Form") 
if button :                      
     st.markdown(f"""
     course :{course}             
     name : {name}
     Rollno : {rno} 
     division : {div} 
     Mother name :{mname} 
     Father Name :{fname} 
     address : {adr} 
     living : {living} 
     
class:{classdata}""")    