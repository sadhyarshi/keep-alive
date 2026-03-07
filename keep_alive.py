import requests
import time
import threading
from datetime import datetime
from tkinter import *

# ── Config ──────────────────────────────────────────
URL = "https://hrms-dbqd.onrender.com/health"
INTERVAL = 5 * 60  # 5 minutes
# ────────────────────────────────────────────────────

running = False
ping_count = 0
success_count = 0
fail_count = 0

def ping():
    global running, ping_count, success_count, fail_count
    while running:
        try:
            res = requests.get(URL, timeout=10)
            now = datetime.now().strftime("%H:%M:%S")
            ping_count += 1
            if res.status_code == 200:
                success_count += 1
                log(f"[{now}]  ✅  Server is awake  —  {res.status_code}", "green")
            else:
                fail_count += 1
                log(f"[{now}]  ⚠️  Unexpected status  —  {res.status_code}", "orange")
        except Exception as e:
            now = datetime.now().strftime("%H:%M:%S")
            ping_count += 1
            fail_count += 1
            log(f"[{now}]  ❌  Failed  —  {e}", "red")

        update_stats()

        for _ in range(INTERVAL):
            if not running:
                break
            time.sleep(1)

def log(msg, color="white"):
    log_box.config(state=NORMAL)
    log_box.insert(END, msg + "\n", color)
    log_box.see(END)
    log_box.config(state=DISABLED)

def update_stats():
    lbl_total.config(text=f"Total Pings: {ping_count}")
    lbl_success.config(text=f"✅ Success: {success_count}")
    lbl_fail.config(text=f"❌ Failed: {fail_count}")

def start():
    global running
    if not running:
        running = True
        btn_start.config(state=DISABLED)
        btn_stop.config(state=NORMAL)
        status_dot.config(fg="lime")
        status_lbl.config(text="Running")
        log(f"Started pinging every 5 minutes...\nURL: {URL}\n", "cyan")
        t = threading.Thread(target=ping, daemon=True)
        t.start()

def stop():
    global running
    running = False
    btn_start.config(state=NORMAL)
    btn_stop.config(state=DISABLED)
    status_dot.config(fg="red")
    status_lbl.config(text="Stopped")
    log("Stopped.\n", "orange")

def clear():
    log_box.config(state=NORMAL)
    log_box.delete(1.0, END)
    log_box.config(state=DISABLED)

# ── UI ──────────────────────────────────────────────
root = Tk()
root.title("HRMS Keep Alive")
root.geometry("600x480")
root.configure(bg="#0f0f1a")
root.resizable(False, False)

# Title
Label(root, text="🚀 HRMS Keep Alive", font=("Arial", 16, "bold"),
      bg="#0f0f1a", fg="white").pack(pady=(18, 2))
Label(root, text=URL, font=("Courier New", 9),
      bg="#0f0f1a", fg="#7c7caa").pack(pady=(0, 12))

# Status bar
status_frame = Frame(root, bg="#0f0f1a")
status_frame.pack()
status_dot = Label(status_frame, text="●", font=("Arial", 14),
                   bg="#0f0f1a", fg="red")
status_dot.pack(side=LEFT, padx=(0, 6))
status_lbl = Label(status_frame, text="Stopped", font=("Arial", 11),
                   bg="#0f0f1a", fg="#aaaacc")
status_lbl.pack(side=LEFT)

# Buttons
btn_frame = Frame(root, bg="#0f0f1a")
btn_frame.pack(pady=14)
btn_start = Button(btn_frame, text="▶  Start", command=start, width=12,
                   bg="#5b21b6", fg="white", font=("Arial", 11, "bold"),
                   relief=FLAT, cursor="hand2", activebackground="#7c3aed")
btn_start.pack(side=LEFT, padx=8)
btn_stop = Button(btn_frame, text="■  Stop", command=stop, width=12,
                  bg="#1f1f2e", fg="#aaaacc", font=("Arial", 11, "bold"),
                  relief=FLAT, cursor="hand2", state=DISABLED)
btn_stop.pack(side=LEFT, padx=8)
btn_clear = Button(btn_frame, text="🗑  Clear", command=clear, width=10,
                   bg="#1f1f2e", fg="#aaaacc", font=("Arial", 11),
                   relief=FLAT, cursor="hand2")
btn_clear.pack(side=LEFT, padx=8)

# Stats
stats_frame = Frame(root, bg="#1a1a2e", pady=8)
stats_frame.pack(fill=X, padx=20, pady=(0, 10))
lbl_total = Label(stats_frame, text="Total Pings: 0", font=("Arial", 10),
                  bg="#1a1a2e", fg="#aaaacc")
lbl_total.pack(side=LEFT, padx=20)
lbl_success = Label(stats_frame, text="✅ Success: 0", font=("Arial", 10),
                    bg="#1a1a2e", fg="lime")
lbl_success.pack(side=LEFT, padx=20)
lbl_fail = Label(stats_frame, text="❌ Failed: 0", font=("Arial", 10),
                 bg="#1a1a2e", fg="#ff6b6b")
lbl_fail.pack(side=LEFT, padx=20)

# Log box
log_box = Text(root, bg="#0d0d1a", fg="white", font=("Courier New", 10),
               state=DISABLED, relief=FLAT, padx=10, pady=8,
               insertbackground="white", height=12)
log_box.pack(fill=BOTH, padx=20, pady=(0, 16), expand=True)
log_box.tag_config("green", foreground="#4ade80")
log_box.tag_config("red", foreground="#f87171")
log_box.tag_config("orange", foreground="#fb923c")
log_box.tag_config("cyan", foreground="#67e8f9")
log_box.tag_config("white", foreground="white")

root.mainloop()