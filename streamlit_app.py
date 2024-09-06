import streamlit as st

import streamlit_antd_components as sac

sac.tabs([
    sac.TabsItem(label='apple', tag="10"),
    sac.TabsItem(icon='google'),
    sac.TabsItem(label='github', icon='github'),
    sac.TabsItem(label='disabled', disabled=True),
], align='center', size='lg' , color='grape', use_container_width=True)
