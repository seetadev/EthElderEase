class QuicStream(INetStream):
    def __init__(self, protocol: QuicConnectionProtocol, stream_id: int):
        self.protocol = protocol
        self.stream_id = stream_id
        self._buffer = bytearray()
        self._event = trio.Event()

    async def read(self, n: int = -1) -> bytes:
        while len(self._buffer) < n or n == -1:
            await self._event.wait()
            self._event = trio.Event()

        if n == -1:
            data = bytes(self._buffer)
            self._buffer.clear()
        else:
            data = bytes(self._buffer[:n])
            self._buffer = self._buffer[n:]
        return data

    async def write(self, data: bytes) -> None:
        self.protocol.send_stream_data(self.stream_id, data)

    async def close(self) -> None:
        self.protocol.close_stream(self.stream_id)

    def data_received(self, data: bytes) -> None:
        self._buffer.extend(data)
        self._event.set()
