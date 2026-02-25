import sys

if sys.platform == "darwin":
    try:
        import AppKit
        info = AppKit.NSBundle.mainBundle().infoDictionary()
        info['LSUIElement'] = '1'
    except ImportError:
        print("Install pyobjc-framework-Cocoa to hide the Dock icon.")

import rumps

WORK_SECONDS = 1500
BREAK_SECONDS = 300

class PomodoroApp(rumps.App):
    def __init__(self):
        super(PomodoroApp, self).__init__(name="Pomodoro", title="🍅")

        self.work = True
        self.seconds_left = WORK_SECONDS
        self.is_running = False
        self.completed_cnt = 0
        self.goal = 3
        
        self.menu = ["Start Timer", "Stop Timer", "Reset", "Completed Today"]

    @rumps.clicked("Start Timer")
    def start_timer(self, _):
        self.is_running = True

    @rumps.clicked("Stop Timer")
    def stop_timer(self, _):
        self.is_running = False

    @rumps.clicked("Reset")
    def reset_timer(self, _):
        self.seconds_left = WORK_SECONDS
        self.is_running = False
        self.work = True
        self.title = "🍅"

    @rumps.clicked("Completed Today")
    def list_completed(self, _):
        rumps.notification(title="Your Progress", subtitle="", message=f"You have completed {self.completed_cnt} Pomodoro sessions today!")

    @rumps.timer(1)
    def timer_start(self, _):
        if not self.is_running:
            return

        if self.seconds_left == 0:
            if self.work:
                self.completed_cnt += 1

                if self.completed_cnt >= self.goal:
                    rumps.notification("Goal Reached!", "🏆", "You've finished 4 sessions!")
                else:
                    rumps.notification("Work Done", "☕️", "Time for a break!")
                
                self.work = False
                self.seconds_left = BREAK_SECONDS
            
            else:
                self.work = True
                self.seconds_left = WORK_SECONDS
                self.is_running = False
                self.title = "🍅"
                rumps.notification("Break is over", "🍅", "Get ready!")

            return

        self.seconds_left -= 1
        mins, secs = divmod(self.seconds_left, 60)
        
        if self.completed_cnt >= self.goal and self.work:
            icon = "🏆"
        elif self.work:
            icon = "🍅"
        else:
            icon = "☕️"

        self.title = f"{icon} {mins:02d}:{secs:02d}"


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()