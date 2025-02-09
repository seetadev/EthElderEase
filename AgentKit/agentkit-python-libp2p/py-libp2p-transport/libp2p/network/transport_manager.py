from libp2p.transport.tcp.tcp import TCP
from libp2p.transport.quic_transport import QuicTransport

DEFAULT_TRANSPORTS = [TCP, QuicTransport]
