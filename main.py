import letters
import time
import os
import random
import string
import subprocess
import datetime


num_of_commits = 1

startdate = datetime.date(2025, 4, 5)
enddate = datetime.date(2026, 1, 1)
dates = [
    [], [], [], [], [], [], []
]
all_dates = [startdate + datetime.timedelta(days=i) for i in range((enddate - startdate).days + 1)]
for d in all_dates:
    dates[(d.weekday() - 1) % 7].append(d)


def print_letters(letter_list: list):
    for i in letter_list:
        for j in i:
            if j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def join_letter(current_list, letter):
    ret = []
    letter_list = letters.alphabet[letter.upper()]
    for i in range(len(current_list)):
        ret.append(current_list[i] + letter_list[i] + [" "])
    return ret


c = [
    [],
    [],
    [],
    [],
    []
]
word = input()
for i in word:
    c = join_letter(c, i)

if len(c[0]) >= 51:
    print(len(c[0]))
    print("Invalid length")
    exit()

print_letters(c)
print(len(c), len(c[0]))


dates_to_commit = []
for w in range(0, 5):
    for i in range(len(c[w])):
        if c[w][i] == 1:
            dates_to_commit.append(dates[w - 1][i])

print(dates_to_commit)
for i in dates_to_commit:
    print(i.weekday())
GIT_COMMAND = ["git", "commit", "-am", "Auto Commit"]

dates_to_commit = sorted(dates_to_commit)

my_env = os.environ.copy()
for date in dates_to_commit:
    author_date = date.strftime("%Y-%m-%d %H:%M")
    my_env["GIT_AUTHOR_DATE"] = author_date
    my_env["GIT_COMMITTER_DATE"] = author_date
    for _ in range(num_of_commits):
        with open("temp.txt", "w") as f:
            text = "".join([random.choice(string.ascii_letters) for _ in range(20)]) + "\n"
            f.write(text)
        subprocess.Popen(GIT_COMMAND, env=my_env).wait(20)
