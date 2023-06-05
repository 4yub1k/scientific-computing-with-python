def add_time(start_time, duration_time, start_day_week=0):
    clock_am_pm = start_time[-2:]
    start_time = list(map(int, start_time[:-2].split(":")))
    duration_time = list(map(int, duration_time.split(":")))

    if start_day_week:
        start_day_week = start_day_week.title()

        week_days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
        # day_of_week = week_days.index(start_day_week)

    if start_time[1] + duration_time[1] > 60:
        duration_time[0] += 1
        duration_time[1] -= 60

    total_time_min = str(start_time[1] + duration_time[1]).zfill(2)

    num_days = 0
    for _ in range(1, duration_time[0] + 1):
        start_time[0] += 1
        if start_time[0] % 12 == 0:
            clock_am_pm = "PM" if clock_am_pm == "AM" else "AM"
            num_days += 1 if clock_am_pm == "AM" else 0
            start_time[0] = 0

    start_time[0] = start_time[0] + 12 if start_time[0] < 1 else start_time[0]

    if start_day_week:
        current_day = 7 - (num_days % 7)

    if num_days == 1:
        if start_day_week:
            return f"{start_time[0]}:{total_time_min} {clock_am_pm}, {week_days[current_day]} (next day)"
        return f"{start_time[0]}:{total_time_min} {clock_am_pm} (next day)"

    elif num_days == 0:
        if start_day_week:
            return f"{start_time[0]}:{total_time_min} {clock_am_pm}, {week_days[0]}"
        return f"{start_time[0]}:{total_time_min} {clock_am_pm}"

    else:
        if start_day_week:
            return f"{start_time[0]}:{total_time_min} {clock_am_pm}, {week_days[current_day - 1]} ({num_days} days later)"
        return f"{start_time[0]}:{total_time_min} {clock_am_pm} ({num_days} days later)"


print(add_time("8:16 PM", "466:02", "tuesday"))
