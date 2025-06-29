import random
import time
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from plyer import notification
from . import messages

console = Console()

break_counter = 0
log_file = os.path.expanduser("~/.teabreak_log")


def pick_random():
    affirmation = random.choice(messages.AFFIRMATIONS)
    suggestion = random.choice(messages.BREAK_SUGGESTIONS)
    return affirmation, suggestion


def tea_mode():
    quote = random.choice(messages.ZEN_QUOTES)
    fact = random.choice(messages.PANDA_FACTS)
    return quote, fact


def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
    except:
        pass


def log_break():
    global break_counter
    break_counter += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Break #{break_counter}\n")


def start_reminder(interval_minutes, enable_tea_mode=False):
    try:
        while True:
            time.sleep(interval_minutes * 60)
            affirmation, suggestion = pick_random()
            title = "🌼 TeaBreak Time! 🌼"
            content = f"{affirmation}\n{suggestion}"

            if enable_tea_mode:
                quote, fact = tea_mode()
                content += f"\nZen: {quote}\nPanda: {fact}"

            console.print(Panel(content, title=title, subtitle=f"Next in {interval_minutes} min", expand=False))
            send_notification("TeaBreak Reminder", affirmation + " | " + suggestion)
            log_break()
    except KeyboardInterrupt:
        console.print("\n[bold green]Thanks for taking care of yourself. See you soon! 💚[/bold green]")