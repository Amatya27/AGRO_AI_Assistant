"""Maps what the user said to a command.

Rules are checked top to bottom and the first match wins, same order as the
original if/elif chain, so phrases like "search linkedin updates" behave the same.
"""

RULES = [
    ("wikipedia", ["wikipedia"]),
    ("translate", ["translate", "translator"]),
    ("youtube", ["open youtube"]),
    ("developer", ["developer", "programmer", "developed", "programmed", "designer", "creator", "created"]),
    ("google", ["open google"]),
    ("search", ["search", "updates on", "update"]),
    ("linkedin", ["linkedin", "linked in"]),
    ("cloud_counselage", ["cloud counselage"]),
    ("email", ["mail", "email"]),
    ("contact", ["contact"]),
    ("week", ["week 1", "week 2", "week 3", "week 4"]),
    ("drl", ["digital resource library", "drl"]),
    ("music", ["music", "song"]),
    ("time", ["the time"]),
    ("code", ["open code"]),
    ("exit", ["exit", "shutdown", "shut down"]),
]


def match(query, enabled=None):
    query = query.lower()
    for name, keywords in RULES:
        if enabled is not None and name not in enabled:
            continue
        if any(k in query for k in keywords):
            return name
    return None
