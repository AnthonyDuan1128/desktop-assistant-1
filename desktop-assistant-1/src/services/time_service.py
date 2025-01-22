class TimeService:
    def __init__(self):
        pass

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def get_current_date(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")