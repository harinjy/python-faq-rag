import streamlit as st
import backend as demo

st.set_page_config(page_title="Python Q&A")

new_title = (
    '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Python Q&A</p>'
)
st.markdown(new_title, unsafe_allow_html=True)

if "vector_index" not in st.session_state:
    with st.spinner("Indexing..."):
        st.session_state.vector_index = demo.python_index()

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("ASK", type="primary")

if go_button:

    with st.spinner("Fetching..."):
        response_content = demo.query_index(
            index=st.session_state.vector_index, question=input_text
        )
        st.write(response_content)
