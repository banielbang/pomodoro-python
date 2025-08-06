import json
import os
import time
from datetime import datetime

STATS_FILE = "data/stats.json"


class PomodoroTimer:
    def __init__(self, work_minutes=25, break_minutes=5):
        self.work = work_minutes * 60
        self.break_time = break_minutes * 60
        self.load_stats()

    def load_stats(self):
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r") as f:
                self.stats = json.load(f)
        else:
            self.stats = {"xp": 0, "streak": 0, "last_date": ""}

    def save_stats(self):
        with open(STATS_FILE, "w") as f:
            json.dump(self.stats, f, indent=4)

    def update_streak(self):
        today = datetime.today().strftime("%Y-%m-%d")
        if self.stats["last_date"] != today:
            self.stats["streak"] += 1
            self.stats["last_date"] = today
        self.save_stats()

    def add_xp(self, amount):
        self.stats["xp"] += amount
        self.save_stats()

    def run_cycle(self):
        print("🕒 Work session started. Focus!")
        self.countdown(self.work)

        print("\n⏸️ Break time. Relax!")
        self.countdown(self.break_time)

        self.add_xp(10)
        self.update_streak()

        print(f"\n✅ XP: {self.stats['xp']} | 🔥 Streak: {self.stats['streak']} day(s)")

    def countdown(self, seconds):
        seconds = int(seconds)  # 👈 force to int
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{int(mins):02d}:{int(secs):02d}"
            print(f"\r⏱️  {timer}", end="")
            time.sleep(1)
            seconds -= 1
