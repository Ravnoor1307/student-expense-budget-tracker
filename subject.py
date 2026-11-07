



import math


class Subject:

    def __init__(self, name, code, faculty, department, credits):
        if not self._is_valid_text(name):
            raise ValueError("Subject name must be a non-empty string.")
        if not self._is_valid_text(code):
            raise ValueError("Subject code must be a non-empty string.")
        if not self._is_valid_text(faculty):
            raise ValueError("Faculty must be a non-empty string.")
        if not self._is_valid_text(department):
            raise ValueError("Department must be a non-empty string.")
        if not self._is_valid_credits(credits):
            raise ValueError("Credits must be a positive number.")

        self.__subject_name = name
        self.__subject_code = code
        self.__faculty = faculty
        self.__department = department
        self.__credits = credits

    @staticmethod
    def _is_valid_text(value):
        return isinstance(value, str) and bool(value.strip())

    @staticmethod
    def _is_valid_credits(value):
        return (
            not isinstance(value, bool)
            and isinstance(value, (int, float))
            and value > 0
            and (isinstance(value, int) or math.isfinite(value))
        )

    def __str__(self):
        return f"Subject Name: {self.__subject_name}, Subject Code: {self.__subject_code}, Faculty: {self.__faculty}, Department: {self.__department}, Credits: {self.__credits}"


    def set_subject_name(self, name):
        if not self._is_valid_text(name):
            return False
        self.__subject_name = name
        return True

    def set_subject_code(self, code):
        if not self._is_valid_text(code):
            return False
        self.__subject_code = code
        return True

    def set_faculty(self, faculty):
        if not self._is_valid_text(faculty):
            return False
        self.__faculty = faculty
        return True

    def set_department(self, department):
        if not self._is_valid_text(department):
            return False
        self.__department = department
        return True

    def set_credits(self, credits):
        if not self._is_valid_credits(credits):
            return False
        self.__credits = credits
        return True

    def get_subject_name(self):
        return self.__subject_name

    def get_subject_code(self):
        return self.__subject_code

    def get_faculty(self):
        return self.__faculty

    def get_department(self):
        return self.__department

    def get_credits(self):
        return self.__credits

    def display_subject_info(self):
        print(f"Subject Name: {self.__subject_name}")
        print(f"Subject Code: {self.__subject_code}")
        print(f"Faculty: {self.__faculty}")
        print(f"Department: {self.__department}")
        print(f"Credits: {self.__credits}")

    def update_faculty(self, new_faculty):
        if not self.set_faculty(new_faculty):
            print("Invalid faculty information provided.")
            return False
        print("Faculty information updated successfully.")
        return True

    def update_subject(self, new_name=None, new_code=None, new_department=None, new_credits=None):
        updates = (
            ("subject name", new_name, self._is_valid_text),
            ("subject code", new_code, self._is_valid_text),
            ("department", new_department, self._is_valid_text),
            ("credits", new_credits, self._is_valid_credits),
        )
        provided_updates = [(name, value) for name, value, _ in updates if value is not None]

        if not provided_updates:
            print("No subject information provided to update.")
            return False

        for name, value, validator in updates:
            if value is not None and not validator(value):
                print(f"Invalid {name} provided; no subject information was updated.")
                return False

        if new_name is not None:
            self.__subject_name = new_name
        if new_code is not None:
            self.__subject_code = new_code
        if new_department is not None:
            self.__department = new_department
        if new_credits is not None:
            self.__credits = new_credits

        print("Subject information updated successfully.")
        return True
