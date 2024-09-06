import streamlit as st

# Create a tab bar
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"])

# Tab 1
with tab1:
    st.header("Tab 1")
    st.write("This is tab 1")

# Tab 2
with tab2:
    st.header("Tab 2")
    st.write("This is tab 2")

# Tab 3
with tab3:
    st.header("Tab 3")
    st.write("This is tab 3")

# Tab 4
with tab4:
    st.header("Tab 4")
    st.write("This is tab 4")

# Tab 5
with tab5:
    st.header("Tab 5")
    st.write("This is tab 5")
