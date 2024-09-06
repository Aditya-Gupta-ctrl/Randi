import streamlit as st

import streamlit_antd_components as sac

sac.tabs([
    sac.TabsItem(label='Home', tag=""),
    sac.TabsItem(icon='google',tag="GPT"),
    sac.TabsItem(label='Python', icon='Python'),
    sac.TabsItem(label='disabled', disabled=True),
], align='center', size='lg' , color='grape', use_container_width=True)
