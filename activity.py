

class Activity:
    def __init__(self,activity_id,title,start_time,end_time,reminder_minutes):
        if not self._is_valid_activity_id(activity_id):
            raise ValueError("Activity ID must be a positive integer.")
        if not self._is_valid_text(title):
            raise ValueError("Title must be a non-empty string.")
        if not self._is_valid_time(start_time):
            raise ValueError("Start time must be a valid time in HH:MM format.")
        if not self._is_valid_time(end_time):
            raise ValueError("End time must be a valid time in HH:MM format.")
        if not self._is_valid_time_range(start_time, end_time):
            raise ValueError("End time must be later than start time.")
        if not self._is_valid_reminder(reminder_minutes):
            raise ValueError("Reminder minutes must be a non-negative integer.")

        self.__activity_id = activity_id
        self.__title = title.strip()
        self.__start_time = start_time
        self.__end_time = end_time
        self.__reminder_minutes = reminder_minutes

    @staticmethod
    def _is_valid_activity_id(value):
        return isinstance(value, int) and not isinstance(value, bool) and value > 0

    @staticmethod
    def _is_valid_text(value):
        return isinstance(value, str) and bool(value.strip())

    @staticmethod
    def _is_valid_time(value):
        if not isinstance(value, str):
            return False
        if len(value) != 5 or value[2] != ":":
            return False
        if not all("0" <= character <= "9" for character in value[:2] + value[3:]):
            return False
        hours = int(value[:2])
        minutes = int(value[3:])
        return 0 <= hours < 24 and 0 <= minutes < 60

    @staticmethod
    def _is_valid_reminder(value):
        return isinstance(value, int) and not isinstance(value, bool) and value >= 0

    @staticmethod
    def _time_to_minutes(value):
        return int(value[:2]) * 60 + int(value[3:])

    @classmethod
    def _is_valid_time_range(cls, start_time, end_time):
        return cls._time_to_minutes(end_time) > cls._time_to_minutes(start_time)

    def __str__(self):
        return f"Activity ID: {self.__activity_id}, Title: {self.__title}, Start Time: {self.__start_time}, End Time: {self.__end_time}, Reminder Minutes: {self.__reminder_minutes}"

    def duration_minutes(self):
        start_parts = self.__start_time.split(":")
        end_parts = self.__end_time.split(":")
        start_minutes = int(start_parts[0]) * 60 + int(start_parts[1])
        end_minutes = int(end_parts[0]) * 60 + int(end_parts[1])
        return end_minutes - start_minutes

    def update_activity(self, new_title=None, new_start_time=None, new_end_time=None, new_reminder_minutes=None):
        if new_title is not None and not self._is_valid_text(new_title):
            return False
        if new_start_time is not None and not self._is_valid_time(new_start_time):
            return False
        if new_end_time is not None and not self._is_valid_time(new_end_time):
            return False
        if (
            new_reminder_minutes is not None
            and not self._is_valid_reminder(new_reminder_minutes)
        ):
            return False

        updated_title = self.__title if new_title is None else new_title.strip()
        updated_start_time = (
            self.__start_time if new_start_time is None else new_start_time
        )
        updated_end_time = self.__end_time if new_end_time is None else new_end_time
        updated_reminder = (
            self.__reminder_minutes
            if new_reminder_minutes is None
            else new_reminder_minutes
        )
        if not self._is_valid_time_range(updated_start_time, updated_end_time):
            return False

        (
            self.__title,
            self.__start_time,
            self.__end_time,
            self.__reminder_minutes,
        ) = (
            updated_title,
            updated_start_time,
            updated_end_time,
            updated_reminder,
        )
        return True

    def get_activity_id(self):
        return self.__activity_id

    def get_title(self):
        return self.__title 

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_reminder_minutes(self):
        return self.__reminder_minutes

    def set_title(self, title):
        if not self._is_valid_text(title):
            return False
        self.__title = title.strip()
        return True     

    def set_start_time(self, start_time):
        if (
            not self._is_valid_time(start_time)
            or not self._is_valid_time_range(start_time, self.__end_time)
        ):
            return False
        self.__start_time = start_time
        return True 

    def set_end_time(self, end_time):
        if (
            not self._is_valid_time(end_time)
            or not self._is_valid_time_range(self.__start_time, end_time)
        ):
            return False
        self.__end_time = end_time
        return True

    def set_reminder_minutes(self, reminder_minutes):
        if not self._is_valid_reminder(reminder_minutes):
            return False
        self.__reminder_minutes = reminder_minutes
        return True

    def display_details(self):
        print(f"Activity ID: {self.__activity_id}")
        print(f"Title: {self.__title}")
        print(f"Start Time: {self.__start_time}")
        print(f"End Time: {self.__end_time}")
        print(f"Reminder Minutes: {self.__reminder_minutes}")
