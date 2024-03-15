"""Main bridge class for Ender."""
import websocket


class EnderConnector:
    """The class."""

    def __init__(self) -> None:
        """init."""
        self._ws: websocket.WebSocketApp | None = None

    def _on_message(self, ws, message):
        """Socket message handler."""
        # print(f"Received message: {message}")

    def _on_error(self, ws, error):
        """Socket error handler."""
        # print(f"Encountered error: {error}")

    def _on_close(self, ws, close_status_code, close_msg):
        """Socket close handler."""
        # print("Connection closed")

    def _on_open(self, ws):
        """Socket open handler."""
        # print("Connection opened")
        ws.send("Hello, Server!")

    def setup(self, host):
        """Connect here."""
        self._ws = websocket.WebSocketApp(
            f"ws://{host}/",
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        self._ws.on_open = self._on_open
        self._ws.run_forever()
