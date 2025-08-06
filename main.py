from pomodoro import PomodoroTimer

if __name__ == "__main__":
    timer = PomodoroTimer(work_minutes=0.05, break_minutes=0.02)  # short test cycle
    timer.run_cycle()
