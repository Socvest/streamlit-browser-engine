import os
import time 
import streamlit as st
from typing import Literal, Optional, Union
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _browser_detection_engine = components.declare_component("browser_detection_engine", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _browser_detection_engine = components.declare_component("browser_detection_engine", path=build_dir)


def browser_detection_engine(timeout:Union[int, float]=5, interval:Union[int, float]=0.1, key:str="browser_engine"):

    """
        Get browser stats like user agent, whether app is running on a desktop, tablet, mobile etc.

        ### Args
            - singleRun (bool): [Defaults to True] Whether to run when component first mounts and only then or if you want it to keep updating when app updates.
    """

    value = _browser_detection_engine(key=key, default=None)
    start_time = time.time()
    while time.time() - start_time < timeout:
        value = st.session_state.get(key)
        if value is not None:
            return value
        time.sleep(interval)
    
    st.warning(f"Timeout reached while waiting for window size information. Using default value: {None}")
    return value

