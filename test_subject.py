
from subject import Subject

# Creating three independent Subject objects
subject1 = Subject("Python Programming", "PY101", "Professor A", "CSE", 4)

subject2 = Subject("Data Structures", "DS102", "Professor B", "CSE", 3)

subject3 = Subject("Mathematics", "MA103", "Professor C", "Mathematics", 5)


# Display original information
print("BEFORE UPDATING")
print(subject1)
print(subject2)
print(subject3)


# Update only subject1
assert subject1.set_faculty("Professor X") is True
assert subject1.set_credits(5) is True

assert subject1.set_faculty("") is False
assert subject1.set_faculty("   ") is False
assert subject1.get_faculty() == "Professor X"

assert subject1.set_subject_name("Python Programming") is True
assert subject1.set_subject_code("PY101") is True
assert subject1.set_department("CSE") is True
assert subject1.set_subject_name("  ") is False
assert subject1.set_subject_code("") is False
assert subject1.set_department(None) is False
assert subject1.set_credits(0) is False
assert subject1.set_credits(-1) is False
assert subject1.set_credits(True) is False
assert subject1.get_credits() == 5

original_subject1 = (
    subject1.get_subject_name(),
    subject1.get_subject_code(),
    subject1.get_department(),
    subject1.get_credits(),
)
assert subject1.update_subject(new_name="Updated name", new_credits=0) is False
assert (
    subject1.get_subject_name(),
    subject1.get_subject_code(),
    subject1.get_department(),
    subject1.get_credits(),
) == original_subject1
assert subject1.update_subject(new_name="Updated name", new_credits=6) is True
assert subject1.get_subject_name() == "Updated name"
assert subject1.get_credits() == 6
assert subject1.update_subject() is False
assert subject1.update_faculty("   ") is False

for invalid_subject in (
    ("", "PY101", "Professor", "CSE", 4),
    ("Python", "  ", "Professor", "CSE", 4),
    ("Python", "PY101", "", "CSE", 4),
    ("Python", "PY101", "Professor", "   ", 4),
    ("Python", "PY101", "Professor", "CSE", 0),
    ("Python", "PY101", "Professor", "CSE", -1),
    ("Python", "PY101", "Professor", "CSE", True),
    ("Python", "PY101", "Professor", "CSE", float("inf")),
):
    try:
        Subject(*invalid_subject)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid subject was accepted: {invalid_subject!r}")

# Display information after updating
print("\nAFTER UPDATING")
print(subject1)
print(subject2)
print(subject3)


# Verify object independence using assertions
assert subject1.get_faculty() == "Professor X"
assert subject1.get_credits() == 6

assert subject2.get_faculty() == "Professor B"
assert subject2.get_credits() == 3

assert subject3.get_faculty() == "Professor C"
assert subject3.get_credits() == 5
assert subject2.get_subject_name() == "Data Structures"
assert subject3.get_subject_name() == "Mathematics"

print("\nAll tests passed!")