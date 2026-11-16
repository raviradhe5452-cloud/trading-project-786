
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI INDEX OPTIONS PRO",
    layout="wide"
)

st.title("🚀 AI INDEX OPTIONS PRO")
st.caption("Advanced Options Trading Dashboard")

market = st.selectbox(
    "Select Index",
    ["NIFTY", "BANKNIFTY", "FINNIFTY", "SENSEX"]
)

st.divider()

st.subheader("Market Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    spot = st.number_input("Spot Price", value=25000.0)

with col2:
    ema = st.number_input("EMA 20", value=25010.0)

with col3:
    vwap = st.number_input("VWAP", value=25005.0)

if spot > ema and spot > vwap and ema > vwap:
    signal = "CALL WATCH"
elif spot < ema and spot < vwap and ema < vwap:
    signal = "PUT WATCH"
else:
    signal = "WAIT"

st.subheader("AI Signal")

if signal == "CALL WATCH":
    st.success("CALL WATCH - Confirmation Pending")
elif signal == "PUT WATCH":
    st.error("PUT WATCH - Confirmation Pending")
else:
    st.warning("WAIT - No Clear Setup")

st.divider()

st.subheader("Risk Management")

capital = st.number_input(
    "Capital ₹",
    min_value=1000,
    value=10000
)

risk_percent = st.slider(
    "Risk Per Trade %",
    0.5, 2.0, 1.0
)

entry = st.number_input("Option Entry Price", value=100.0)
sl_percent = st.number_input("Stop Loss %", value=10.0)
target_percent = st.number_input("Target %", value=20.0)

risk_amount = capital * risk_percent / 100
stop_loss = entry * (1 - sl_percent / 100)
target = entry * (1 + target_percent / 100)

c1, c2, c3 = st.columns(3)

c1.metric("Maximum Planned Risk", f"₹{risk_amount:.2f}")
c2.metric("Stop Loss Price", f"₹{stop_loss:.2f}")
c3.metric("Target Price", f"₹{target:.2f}")

st.divider()

st.subheader("Trading Status")
st.info("PAPER TRADING MODE - No real orders")

st.caption(
    "Version 2.0 | Live market data connection pending"
)
