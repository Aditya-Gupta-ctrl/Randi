import streamlit as st

import streamlit_antd_components as sac

sac.tabs([
    sac.TabsItem(label='Home', tag=""),
    sac.TabsItem(icon='google'),
    sac.TabsItem(label='C++', icon='C++'),
    sac.TabsItem(label='disabled', disabled=True),
], align='center', size='lg' , color='grape', use_container_width=True)
