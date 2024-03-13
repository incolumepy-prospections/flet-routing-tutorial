"""State module."""


class State:
    """State class."""

    def __init__(self, key: str, value: str | None = None):
        """Init class."""
        self._global_state = global_state
        self._key = key
        self._value = value
        self.register_with_global()

    def register_with_global(self):
        """Register global."""
        self._global_state.register_state(self)

    def get_key(self):
        """Get key."""
        return self._key

    def get_state(self):
        """Get state."""
        return self._value


class GlobalState:
    """GlobalState class."""

    def __init__(self):
        """Init for class."""
        self._state = {}

    def register_state(self, state: State) -> None:
        """Register stage function."""
        self._state[state.get_key()] = state

    def get_state_by_key(self, key: str) -> State:
        """Get state by key."""
        return self._state.get(key)


global_state = GlobalState()
