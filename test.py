import re


def is_valid_entry(s):
    pattern = r'^\d{1,3}:\d{1,3}$'
    return bool(re.match(pattern, s))


def parse_time_entry():
    entries = ["9:9", "10:01", "123:45", "999:99",
               "1234:56", "10:999", "abc:12", "12:"]
    for entry in entries:
        if is_valid_entry(entry):
            minutes, seconds = map(int, entry.strip().split(":"))
            print("valid", minutes, seconds)

# Test examples
test_cases = ["9:9", "10:01", "123:45", "999:99",
              "1234:56", "10:999", "abc:12", "12:"]

# for case in test_cases:
#     print(f"{case:10} -> {is_valid_entry(case)}")

parse_time_entry()


time_left

def a():
    global time_left
    # code
    b()
    # more code

def b():
    global time_left
    # more code