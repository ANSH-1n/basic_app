#1.---BASIC OF SSTREAMLIT MODULE
# import streamlit as st 
# st.title("welcome to my website")
# st.header('python')
# st.subheader('java')
# st.markdown('i love python') #markdown show the data on user interface of website
# st.code("""for i in range(1,5,1):
#        print("hello) """)


import streamlit as st
name = st.text_input("Enter your name:")
f_name = st.text_input("Enter your father name:")
address = st.text_area("Enter your adress:")
classdata = st.selectbox("Enter your class:",(1,2,3,4,5,6))

button =st.button("Done")
if button:
    st.markdown(f"""
     Name : {name}
     father Name: {f_name}    
     Address : {address}
     class : {classdata}           
                 """)