import streamlit as st
import bedrock as glib

st.set_page_config(page_title="Text to Text")
st.title("Text to Text")


input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("Go", type="primary")

if go_button:
    
    with st.spinner("Working..."):
        response_content = glib.get_text_response(input_content=input_text)
        
        st.write(response_content) 


# streamlit run web.py --server.port 8080