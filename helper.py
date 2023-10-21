import streamlit as st

def get_author_info():
    st.write("Format of auther deatils")
    st.markdown("- Author name")
    st.markdown("- Name of Depatment")
    st.markdown("- Name of Orgnasition")
    st.markdown("- Email id")
    with st.expander("Enter author details"):
        aut = st.slider('Enter the number of authors:', 1, 5,3)
        authors_info = []
        for i in range(aut):
            name = st.text_area(f"Auther {i+1}:", key=f"name_{i}")
            authors_info.append(name)

    return authors_info

def get_ref():
    with st.expander("Enter references"):
        age = st.number_input('Enter the number of authors:', 1, 50,5)
        ref_info = []
        for i in range(age):
            name = st.text_input(f"Ref {i+1}:", key=f"ref_{i}")
            ref_info.append(name)

    return ref_info



    




