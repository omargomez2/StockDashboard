# 📊 Dividend Stock Dashboard with LLM Insights

This project is an interactive financial dashboard built using **Streamlit**, **yFinance**, and **OpenRouter**. It allows users to visualize historical price data of dividend stocks (like Coca-Cola, Pepsi, etc.), view company fundamentals, and query a large language model (LLM) for investment insights.

---

## 🚀 Features

- ✅ Enter any stock symbol (e.g., `KO`, `PEP`, `PG`)
- ✅ View recent candlestick chart with Plotly
- ✅ Explore company summary, sector, dividend yield, and market cap
- ✅ Ask the LLM questions like:
  - *Is this a good time to buy Coca-Cola?*
  - *What are the dividend trends of Pepsi?*

---

## 🧠 Powered by OpenRouter LLM

The app uses [`deepseek-chat`](https://openrouter.ai/deepseek/deepseek-chat) model through OpenRouter's API to answer questions about the selected stock.

---

## 📦 Requirements

```bash
pip install -r requirements.txt
