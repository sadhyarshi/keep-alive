# 🚀 URL Health Monitor

A lightweight desktop application built with Python to monitor the health of any URL and keep it alive by pinging it at regular intervals.

---

## Project Overview

URL Health Monitor is a simple yet powerful desktop tool that continuously pings a configured URL every 5 minutes and displays real-time status logs. It is especially useful for keeping free-tier hosted backends (like Render, Railway, etc.) alive by preventing them from spinning down due to inactivity.

The application features a clean dark-themed GUI built with Python's built-in `tkinter` library — no heavy frameworks needed.

---

## Features

- Live ping status with timestamp logs
- Start / Stop monitoring with a single click
- Real-time stats — Total Pings, Success, Failed
- Color-coded logs — green for success, red for failure
- Runs in background using threading — UI stays responsive
- Zero external UI dependencies — uses built-in tkinter

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core language |
| Tkinter | GUI (built-in, no install needed) |
| Requests | HTTP ping requests |
| Threading | Background ping without freezing UI |

---

## Project Structure

```
keep-alive/
├── keep_alive.py    # Main application file
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11+

### Installation

```bash
git clone https://github.com/sadhyarshi/keep-alive.git
cd keep-alive
pip install requests
```

### Run

```bash
python keep_alive.py
```

A desktop window will open. Click **▶ Start** to begin monitoring.

---

## Configuration

To monitor your own URL, open `keep_alive.py` and update the config at the top:

```python
URL = "https://your-url.onrender.com/health"
INTERVAL = 5 * 60  # ping every 5 minutes
```

---

## How It Works

1. Click **▶ Start** — a background thread starts pinging the URL every 5 minutes
2. Each ping result is logged with a timestamp in the log window
3. Stats (Total, Success, Failed) update after every ping
4. Click **■ Stop** to stop monitoring at any time
5. Click **🗑 Clear** to clear the log window

---

## Use Case

Free hosting platforms like **Render** spin down inactive services after 15 minutes. This tool pings your backend every 5 minutes to keep it awake — no paid plan needed.

---

## License

This project is for educational and personal use.