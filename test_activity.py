from activity import Activity


def create_activity(activity_id):
    return Activity(activity_id, "Study", "09:00", "10:00", 5)


for valid_id in (101, 1):
    activity = create_activity(valid_id)
    assert activity.get_activity_id() == valid_id

for invalid_id in (0, -5, True, "101"):
    try:
        create_activity(invalid_id)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid activity ID was accepted: {invalid_id!r}")

for start_time, end_time in (("07:30", "08:00"), ("00:00", "00:01"), ("23:58", "23:59")):
    activity = Activity(1, "Study", start_time, end_time, 5)
    assert activity.get_start_time() == start_time
    assert activity.get_end_time() == end_time

for invalid_time in (
    "7:30",
    "07:3",
    "25:00",
    "10:75",
    "07:30:00",
    "a7:30",
    "07:a0",
    "0 :30",
    "٠٧:30",
):
    try:
        Activity(1, "Study", invalid_time, "10:00", 5)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid time was accepted: {invalid_time!r}")

for reminder in (5, 0):
    assert Activity(1, "Study", "09:00", "10:00", reminder).get_reminder_minutes() == reminder

for reminder in (-1, True, 2.5, "5"):
    try:
        Activity(1, "Study", "09:00", "10:00", reminder)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid reminder was accepted: {reminder!r}")

activity = Activity(1, "Study", "07:00", "08:00", 5)
assert activity.duration_minutes() == 60
for start_time, end_time in (("10:00", "09:00"), ("10:00", "10:00")):
    try:
        Activity(1, "Study", start_time, end_time, 5)
    except ValueError:
        pass
    else:
        raise AssertionError(
            f"Invalid start/end relationship was accepted: {start_time}–{end_time}"
        )

assert activity.set_start_time("08:00") is False
assert activity.set_end_time("07:00") is False
assert activity.get_start_time() == "07:00"
assert activity.get_end_time() == "08:00"
assert activity.set_reminder_minutes(True) is False
assert activity.get_reminder_minutes() == 5

assert activity.update_activity(new_start_time="08:00", new_end_time="09:00") is True
assert activity.get_start_time() == "08:00"
assert activity.get_end_time() == "09:00"

before_invalid_update = (
    activity.get_title(),
    activity.get_start_time(),
    activity.get_end_time(),
    activity.get_reminder_minutes(),
)
assert activity.update_activity(
    new_title="Advanced Python",
    new_start_time="09:00",
    new_end_time="10:0",
) is False
assert (
    activity.get_title(),
    activity.get_start_time(),
    activity.get_end_time(),
    activity.get_reminder_minutes(),
) == before_invalid_update

assert activity.update_activity(
    new_title="Advanced Python",
    new_start_time="09:00",
    new_end_time="08:30",
) is False
assert (
    activity.get_title(),
    activity.get_start_time(),
    activity.get_end_time(),
    activity.get_reminder_minutes(),
) == before_invalid_update
assert activity.update_activity(new_reminder_minutes=True) is False
assert activity.get_reminder_minutes() == 5

print("All activity validation tests passed!")
