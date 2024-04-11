# streamlit-browser-engine

Streamlit component that allows you to get browser stats like user agent or whether the app is being run on mobile or desktop or if you are using Chrome, Firefox, IE etc and more.

## Installation instructions

```sh
pip install streamlit-browser-engine
```

## Usage instructions

```python
import streamlit as st
from browser_detection import browser_detection_engine

value = browser_detection_engine()
st.write(value)

```

params:
- singleRun [defaults to True] - if you only want component to run when app first runs. It will only run once and get the data once. Use False if you want to run everytime app re-runs. 
