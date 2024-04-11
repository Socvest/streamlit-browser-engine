import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"
import BrowserDetector from 'browser-dtector'


const BrowserDetection: React.FC<ComponentProps> = (props: any) => {

  const { args } = props
  const singleRun: any = args["singleRun"]

  const browser = new BrowserDetector(window.navigator.userAgent);

  useEffect(() => {
    Streamlit.setFrameHeight(0)
  })

  useEffect(() => {
    if (!singleRun) {
      Streamlit.setComponentValue(browser.parseUserAgent())
    }

  })
  useEffect(() => {

    if (singleRun) {
      Streamlit.setComponentValue(browser.parseUserAgent())
      Streamlit.setComponentReady()
    }

  }, [])

  return (
    <div style={{ display: "none" }}>
    </div>
  )

}



export default withStreamlitConnection(BrowserDetection)