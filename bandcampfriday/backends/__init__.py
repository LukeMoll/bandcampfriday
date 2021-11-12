from .messagebackend import AbstractMessageBackend

from .slackwebhook import SlackWebhook

_backends = [SlackWebhook]

def available_backends() -> list[str]:
    return list(map(lambda c: c.__name__, _backends))

def get_backend(s: str) -> AbstractMessageBackend:
    for b in _backends:
        if b.__name__ == s:
            return b()
    return KeyError(s+" is not a message backend")