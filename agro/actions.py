import datetime
import os
import random
import subprocess
import sys
import webbrowser

from . import config


def greeting(hour):
    if hour < 12:
        return "Good Morning"
    if hour < 18:
        return "Good Afternoon"
    return "Good Evening"


def open_url(url):
    webbrowser.open(url)


def open_path(path):
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def wikipedia_summary(voice, query):
    voice.say("Searching Wikipedia...")
    topic = query.replace("wikipedia", "").strip()
    try:
        import wikipedia
        result = wikipedia.summary(topic, sentences=2)
    except Exception:
        voice.say(f"Sorry sir, I couldn't find a clear Wikipedia answer for {topic}.")
        return
    voice.say("According to Wikipedia")
    voice.say(result)


def youtube(voice, query):
    voice.say("Opening Youtube...")
    open_url(config.LINKS["youtube"])


def developer(voice, query):
    voice.say("AGRO is an AI Powered Chatbot developed by Amatya Katyayan")
    open_url(config.DEVELOPER_LINKEDIN)
    voice.say("You can know more about Amatya Katyayan using this LinkedIn Page")


def google(voice, query):
    voice.say("Opening Google...")
    open_url(config.LINKS["google"])


def web_search(voice, query):
    voice.say("Importing Information and Acquiring relevant data...")
    terms = query.replace("search", "").strip()
    try:
        from googlesearch import search
    except ImportError:
        open_url("https://www.google.com/search?q=" + "+".join(terms.split()))
        return
    try:
        results = list(search(terms, num_results=3))
    except TypeError:
        results = list(search(terms, tld="co.in", num=3, stop=3, pause=2))
    for url in results[:3]:
        open_url(url)


def linkedin(voice, query):
    voice.say("Opening LinkedIn...")
    open_url(config.LINKS["cc_linkedin"])


def cloud_counselage(voice, query):
    voice.say("Opening Homepage...")
    open_url(config.LINKS["cc_home"])


def email(voice, query):
    voice.say("Opening Email...")
    open_url(config.LINKS["cc_email"])


def contact(voice, query):
    voice.say("Opening Webpage...")
    open_url(config.LINKS["cc_contact"])
    voice.say("You can contact us using any of the options available on the web page.")


def week(voice, query):
    for key, (title, url) in config.WEEKS.items():
        if key in query:
            voice.say(f"Opening {title}...")
            open_url(url)
            return


def drl(voice, query):
    voice.say("Opening Digital Resource Library...")
    open_url(config.LINKS["drl"])


def music(voice, query):
    try:
        songs = [f for f in os.listdir(config.MUSIC_DIR) if not f.startswith(".")]
    except FileNotFoundError:
        songs = []
    if not songs:
        voice.say(f"I couldn't find any songs in {config.MUSIC_DIR}. You can set AGRO_MUSIC_DIR.")
        return
    open_path(os.path.join(config.MUSIC_DIR, random.choice(songs)))


def tell_time(voice, query):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    voice.say(f"Sir, the time is {now}")


def open_code(voice, query):
    try:
        subprocess.Popen([config.VSCODE])
    except OSError:
        voice.say("I couldn't start VS Code. Set AGRO_VSCODE to its path.")


def shutdown(voice, query):
    voice.say("Lowering power modules and shutting down the system. Hope you have a great day sir")
    return False


HANDLERS = {
    "wikipedia": wikipedia_summary,
    "youtube": youtube,
    "developer": developer,
    "google": google,
    "search": web_search,
    "linkedin": linkedin,
    "cloud_counselage": cloud_counselage,
    "email": email,
    "contact": contact,
    "week": week,
    "drl": drl,
    "music": music,
    "time": tell_time,
    "code": open_code,
    "exit": shutdown,
}
