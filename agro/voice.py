class Voice:
    """Speaks and listens. In text mode (or when no mic/TTS is available) it uses the terminal."""

    def __init__(self, text_mode=False):
        self.text_mode = text_mode
        self._engine = None
        if not text_mode:
            try:
                import pyttsx3
                self._engine = pyttsx3.init()
            except Exception as exc:
                print(f"(text-to-speech unavailable, printing instead: {exc})")

    def say(self, text, show=True):
        if show:
            print(f"AGRO: {text}")
        if self._engine:
            self._engine.say(text)
            self._engine.runAndWait()

    def listen(self, language="en-in"):
        if self.text_mode:
            try:
                return input("You: ").strip()
            except EOFError:
                return "exit"

        import speech_recognition as sr

        recognizer = sr.Recognizer()
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 500
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language=language)
            print(f"You said: {query}\n")
            return query
        except Exception:
            print("Pardon me sir, please try again...")
            return ""
