class Observer:
    def update(self, message):
        pass


class LoggerObserver(Observer):
    def update(self, message):
        print(f"[LOG] {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, obs):
        self._observers.append(obs)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)
