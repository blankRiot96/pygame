from typing import List

from pygame.event import Event

def init() -> None: ...
def get_init() -> bool: ...
def pump() -> None: ...
def wait() -> Event: ...
def poll() -> Event: ...
def get() -> List[Event]: ...
def post(event: Event) -> None: ...
