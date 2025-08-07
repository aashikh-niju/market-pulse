




# Market Pulse 📊

A full-stack web app that delivers financial insights and news using AI and real-time APIs.

## 🚀 Features
- 📈 Market data from **Alpha Vantage API**
- 📰 Financial news using **GNews API**
- 🤖 AI response using **Gemini API** (currently not working – quota limit reached)
- 🔗 Frontend–Backend integration complete

## 🛠️ Technologies Used
- React (Frontend)
- Flask (Backend)
- Alpha Vantage API
- GNews API
- Gemini API (partially implemented)

## ⚙️ Setup

### Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # or source .venv/bin/activate on Linux/macOS
pip install -r requirements.txt
python app.py
````

### Frontend

```bash
cd frontend
npm install
npm start
```

## 📝 Notes

* Gemini API returns: **"limit reached"**, so fallback APIs are in place.
* Successfully connected the backend and frontend.
* Focused on completing a **runnable slice** within 4 hours.
* **Stretch goals** like advanced AI response handling, error management, and UI polish can be added later.

---

⏱️ **Duration**: \~4 hours
✅ MVP functional with two working APIs
❌ Gemini API issue due to quota exhaustion



Let me know if you'd like a demo GIF section or project screenshots added too!
```
