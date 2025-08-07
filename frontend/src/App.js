import React, { useState } from "react";
import axios from "axios";

function App() {
  const [ticker, setTicker] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const fetchData = async () => {
    try {
      setError("");
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/stock-price?ticker=${ticker}`);
      setData(response.data);
    } catch (err) {
      setError("Error fetching data. Please check the backend.");
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h2>📊 Market Pulse</h2>
      <input
        type="text"
        placeholder="Enter Stock Ticker (e.g., AAPL)"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      />
      <button onClick={fetchData} style={{ marginLeft: "1rem" }}>
        Get Signal
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Results for {data.ticker}</h3>
          <p><strong>Last 5 Closing Prices:</strong> {data.last_5_closing_prices.join(", ")}</p>
          <p><strong>Daily Returns:</strong> {data.daily_returns.join(", ")}</p>
          <p><strong>Momentum Score:</strong> {data.momentum_score}</p>
          <p><strong>Pulse:</strong> {data.pulse}</p>
          <p><strong>LLM Explanation:</strong> {data.llm_explanation}</p>
          <h4>📰 News</h4>
          <ul>
            {data.news.map((item, index) => (
              <li key={index}>
                <a href={item.url} target="_blank" rel="noopener noreferrer">
                  <strong>{item.title}</strong>
                </a>
                <p>{item.description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
