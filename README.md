# 🍅 macOS Pomodoro Widget

A lightweight, native macOS menu bar application designed for deep work. This utility stays entirely in your status bar, providing a distraction-free countdown timer that integrates directly with the macOS ecosystem.

## 1. Project Overview
This widget is a specialized productivity tool that lives in the macOS menu bar. Unlike standard applications, it operates as a "Background Agent," meaning it has no Dock icon and does not appear in the `Cmd + Tab` switcher, keeping your workspace clean while you focus on coding.



## 2. Key Features
* **Native UI:** Built with the `rumps` framework for a seamless, "Apple-native" look and feel.
* **Background Agent Mode:** Uses `AppKit` logic to hide from the Dock and task switcher.
* **Dynamic Session States:** Automatically toggles between **Focus sessions (🍅)** and **Break periods (☕️)**.
* **System Integration:** Uses the macOS Notification Center to alert you when a session ends.
* **Low Resource Usage:** Written in Python with minimal dependencies to ensure it doesn't impact system performance.

## 3. Technical Implementation
As a Computer Science project, this focuses on clean process management and OS-level integration:
* **Language:** Python 3.12+
* **OS Bridge:** Uses `PyObjC` to communicate with the macOS Cocoa framework.
* **Process Decoupling:** Implements a `disown` pattern in the launcher script to allow the app to survive after the terminal is closed.
* **State Management:** A custom event loop handles the countdown without blocking the UI thread.



## 4. Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ronioz/pomodoroWidget
    cd pomodoroWidget
    ```

2.  **Initialize the Environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python3 main.py
    ```

## 5. Project Structure
* `main.py`: Core application logic and UI event loop.
* `.gitignore`: Excludes environment binaries, Python caches, and macOS metadata.
* `requirements.txt`: List of necessary Python dependencies.

---