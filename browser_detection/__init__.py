import os
import streamlit as st
import streamlit.components.v1 as components


_RELEASE = True

if not _RELEASE:
    _browser_detection_engine = components.declare_component("browser_detection_engine", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _browser_detection_engine = components.declare_component("browser_detection_engine", path=build_dir)


def browser_detection_engine(singleRun:bool=False, key:str="browser_engine"):

    """
        Get browser stats like user agent, whether app is running on a desktop, tablet, mobile etc.

        ### Args
            - singleRun (bool): [Defaults to True] Whether to run when component first mounts and only then or if you want it to keep updating when app updates.
    """

    value = _browser_detection_engine(singleRun=singleRun, key=key, default={})

    return value

