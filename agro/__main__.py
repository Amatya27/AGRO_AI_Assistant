import argparse
import datetime

from . import actions, config, intents
from .voice import Voice


def handle(voice, query):
    """Runs one command. Returns False when the assistant should stop."""
    query = query.lower()
    name = intents.match(query, enabled=actions.HANDLERS.keys())
    if name is None:
        return True
    return actions.HANDLERS[name](voice, query) is not False


def main(argv=None):
    parser = argparse.ArgumentParser(prog="agro", description="AGRO voice assistant")
    parser.add_argument("--text", action="store_true", help="type commands instead of speaking them")
    args = parser.parse_args(argv)

    voice = Voice(text_mode=args.text)
    voice.say(actions.greeting(datetime.datetime.now().hour))
    voice.say("Hello sir, this is AGRO at your service. We are online and ready. How can I assist you?")

    while handle(voice, voice.listen(config.SPEECH_LANGUAGE)):
        pass


if __name__ == "__main__":
    main()
