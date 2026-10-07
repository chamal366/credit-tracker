class Time:
    def __init__ (self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_seconds = self.second + other.second
        extra_minutes = total_seconds // 60
        total_seconds %= 60

        total_minutes = self.minute + other.minute + extra_minutes
        extra_hours = total_minutes // 60
        total_minutes %= 60

        total_hours = self.hour + other.hour + extra_hours
        return Time(total_hours, total_minutes, total_seconds)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

times = []
    
for i in range(2):
    hour = int(input(f"Enter the hour for time {i+1}: "))
    minute = int(input(f"Enter the minute for time {i+1}: "))  
    second = int(input(f"Enter the second for time {i+1}: "))
    times.append(Time(hour, minute, second))

obj1 = times[0]
obj2 = times[1] 
ob3 = obj1 + obj2
print("Time 1:", obj1)
print("Time 2:", obj2)
print("Sum of Time 1 and Time 2:", ob3)