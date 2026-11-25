import pytest

from agro import __main__ as app
from agro import actions, intents


class FakeVoice:
    def __init__(self):
        self.said = []

    def say(self, text, show=True):
        self.said.append(text)


@pytest.fixture
def opened(monkeypatch):
    urls = []
    monkeypatch.setattr(actions, "open_url", urls.append)
    return urls


@pytest.mark.parametrize("query, expected", [
    ("wikipedia alan turing", "wikipedia"),
    ("open youtube please", "youtube"),
    ("who is your developer", "developer"),
    ("open google", "google"),
    ("search robotics jobs", "search"),
    ("any updates on the stock market", "search"),
    ("open linked in", "linkedin"),
    ("tell me about cloud counselage", "cloud_counselage"),
    ("send an email", "email"),
    ("how do I contact you", "contact"),
    ("open week 3", "week"),
    ("open the drl", "drl"),
    ("play a song", "music"),
    ("what is the time", "time"),
    ("open code", "code"),
    ("shut down", "exit"),
    ("hello there", None),
])
def test_match(query, expected):
    assert intents.match(query) == expected


def test_first_rule_wins_like_the_original_chain():
    # "search" comes before "linkedin" in the original if/elif order
    assert intents.match("search linkedin updates") == "search"


@pytest.mark.parametrize("hour, text", [(0, "Good Morning"), (11, "Good Morning"), (12, "Good Afternoon"), (17, "Good Afternoon"), (18, "Good Evening")])
def test_greeting(hour, text):
    assert actions.greeting(hour) == text


def test_week_opens_the_right_task(opened):
    voice = FakeVoice()
    assert app.handle(voice, "Open Week 2")
    assert opened == [actions.config.WEEKS["week 2"][1]]
    assert voice.said == ["Opening Week 2 - Advance Training..."]


def test_developer_opens_linkedin(opened):
    app.handle(FakeVoice(), "who created you")
    assert opened == [actions.config.DEVELOPER_LINKEDIN]


def test_exit_stops_the_loop(opened):
    assert app.handle(FakeVoice(), "exit") is False


def test_unknown_command_keeps_running(opened):
    assert app.handle(FakeVoice(), "") is True
    assert opened == []


def test_music_with_empty_folder(tmp_path, monkeypatch):
    monkeypatch.setattr(actions.config, "MUSIC_DIR", str(tmp_path))
    voice = FakeVoice()
    actions.music(voice, "play music")
    assert "couldn't find any songs" in voice.said[0]
