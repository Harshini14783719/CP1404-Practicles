from datetime import datetime


class Project:

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completion_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority
