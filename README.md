# AI-Powered Stock News Sentiment Dashboard

## Overview
This project is a real-time financial analytics system that combines streaming stock prices with live news headlines and applies AI sentiment analysis to detect how media sentiment impacts short-term stock price movements. 

Built using **Python**, **SQLite**, and **Tableau**, the system ingests real-time stock price updates from Yahoo Finance’s WebSocket and matches them with news headlines from NewsAPI/NYTimes. A sentiment model analyzes each headline, and the results are visualized in an interactive Tableau dashboard.

---

## Features
- Real-time stock price ingestion from Yahoo Finance
- Real-time news headline ingestion
- AI sentiment analysis using Python (VADER)
- SQLite database for storing stock and news data
- Tableau Public dashboard visualization
- CSV export for further analysis

---

## Tech Stack
- **Python** – data ingestion, ETL, sentiment analysis  
- **SQLite** – storage of stock and news data  
- **VADER (NLP)** – sentiment scoring of headlines  
- **Tableau Public** – interactive dashboard  
- **GitHub** – project hosting and version control  

---

## Architecture
1. **Stock Price Script (`src/websocket_prices.py`)**  
   Connects to Yahoo Finance WebSocket and stores stock prices in SQLite.

2. **News Script (`src/fetch_news.py`)**  
   Fetches news headlines from NewsAPI or NYTimes and stores them with sentiment scores.

3. **Sentiment Script (`src/sentiment_model.py`)**  
   Applies VADER sentiment analysis to each headline and labels it as positive, negative, or neutral.

4. **Merge Script (`src/merge_data.py`)**  
   Merges stock prices and news sentiment by timestamp and exports CSV for Tableau.

5. **Tableau Dashboard**  
   Visualizes price vs sentiment over time, sentiment spikes, and top headl
