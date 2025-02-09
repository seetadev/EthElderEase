import pytest
from libp2p.peer.id import ID
from libp2p.transport.quic_transport import QuicTransport, QuicStream
from multiaddr import Multiaddr
import trio

@pytest.mark.asyncio
async def test_quic_transport_dial_and_listen():
    transport = QuicTransport()
    peer_id = ID.from_string("QmPeerId")
    multiaddr = Multiaddr("/ip4/127.0.0.1/udp/12345/quic")

    stream = await transport.dial(peer_id, multiaddr)
    assert stream is not None

    listener = await transport.listen(multiaddr)
    assert listener is not None

    await listener.stop()

@pytest.mark.asyncio
async def test_quic_stream_read_write():
    transport = QuicTransport()
    peer_id = ID.from_string("QmPeerId")
    multiaddr = Multiaddr("/ip4/127.0.0.1/udp/12345/quic")

    stream = await transport.dial(peer_id, multiaddr)
    assert stream is not None

    test_data = b"hello, quic!"
    await stream.write(test_data)

    if isinstance(stream, QuicStream):
        stream.data_received(test_data)

    received_data = await stream.read()
    assert received_data == test_data

    await stream.close()
