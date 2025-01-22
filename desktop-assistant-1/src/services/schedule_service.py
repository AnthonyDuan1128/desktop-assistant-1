class ScheduleService:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, event):
        self.schedules.append(event)

    def remove_schedule(self, event):
        if event in self.schedules:
            self.schedules.remove(event)

    def view_schedules(self):
        return self.schedules

    def clear_schedules(self):
        self.schedules.clear()