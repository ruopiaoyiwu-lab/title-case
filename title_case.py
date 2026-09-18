# Git Bootcamp reference code. reference/README.md says which file goes with
# which exercise step. Copy it as-is; the code is only a vehicle for Git, so
# your own version is equally fine.


def my_cap(text):
    return text[0].upper() + text[1:]


def my_title(text):
    words = []
    for t in text.split():
        words.append(my_cap(t))
    return " ".join(words)
