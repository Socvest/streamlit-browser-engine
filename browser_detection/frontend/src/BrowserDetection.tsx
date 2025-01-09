import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect, useMemo } from "react"
import BrowserDetector from 'browser-dtector'


const BrowserDetection: React.FC<ComponentProps> = (props: any) => {

  const { args } = props
  const browser = useMemo(() => new BrowserDetector(window.navigator.userAgent), []); 

  useEffect(() => {
    Streamlit.setFrameHeight(0)
  })

  useEffect(() => {
    Streamlit.setComponentValue(browser.parseUserAgent())
    Streamlit.setComponentReady()

  }, [browser]) 

  return <></>

}



export default withStreamlitConnection(BrowserDetection)
