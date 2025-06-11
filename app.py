import os
import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set up OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Function to fetch dividend stock data
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="6mo")
    info = stock.info
    return hist, info

# LLM Query
def ask_llm(question, symbol):
    prompt = f"You are a financial assistant. Based on current market context, data for {symbol}, and historical trends, answer the following: {question}"
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ LLM failed: {e}"

# Streamlit UI
st.set_page_config(page_title="Dividend Stock Dashboard", layout="wide")
st.title("📈 Dividend Stock Dashboard")

symbol = st.text_input("Enter stock symbol (e.g., KO for Coca-Cola):", value="KO")

if symbol:
    hist, info = fetch_stock_data(symbol)

    st.subheader(f"Overview of {symbol.upper()}")
    st.write(f"**Company Name:** {info.get('longName', 'N/A')}")
    st.write(f"**Sector:** {info.get('sector', 'N/A')}")
    st.write(f"**Dividend Yield:** {info.get('dividendYield', 'N/A')}")
    st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}")
    st.write(f"**Summary:** {info.get('longBusinessSummary', 'No summary available.')}")

    # Candlestick Chart
    st.subheader("Stock Price - Last 6 Months")
    fig = go.Figure(data=[go.Candlestick(
        x=hist.index,
        open=hist['Open'],
        high=hist['High'],
        low=hist['Low'],
        close=hist['Close']
    )])
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    # Ask LLM
    st.subheader("💬 Ask AI for Buy Insight")
    user_question = st.text_area("What do you want to know about this stock?", value="Is this a good time to buy?")
    
    if st.button("Ask AI"):
        with st.spinner("Thinking..."):
            answer = ask_llm(user_question, symbol)
            st.markdown(f"**AI Response:**\n\n{answer}")