# AgentKit Track

This directory contains code and documentation for the AgentKit track of the ElderEase project.

ElderEase is an AI-powered concierge, home maintenance, and cleaning service designed for elderly care users. It integrates AgentKit to enable seamless Web3 payments and on-chain interactions through Agentic Ethereum. By leveraging AgentKit, we empower AI agents to manage service requests, process transactions, and interact with decentralized protocols—abstracting away Web3 complexities for elderly users.

How We Are Using AgentKit

1. AI-Driven On-Chain Payments
- We utilize AgentKit’s wallet integration to facilitate payments in FIL, ETH, and ERC-20 tokens for home maintenance, cleaning, and concierge services.
- AI agents autonomously execute transactions based on user requests, making payments gas-efficient and seamless.
- Smart contract interactions for service deposits and refunds ensure trustless payments.

2. Autonomous Web3 Agent Interactions
- ElderEase’s AI concierge uses AgentKit's on-chain action execution to interact with service providers, confirming bookings and triggering payments.
- The agent also verifies service completion using IPFS-stored records and sends proof to an Ethereum smart contract.
- Users interact with agents via Alexa Skills, voice commands, and mobile apps—AgentKit ensures smooth on-chain execution.

3. Multi-Agent Collaboration with Agentic Ethereum
- Multi-agent systems coordinate home maintenance and emergency assistance, exchanging data via Nethermind’s dotnet libp2p.
- When urgent maintenance or road assistance is required, an agent:
- Identifies the issue via TinyYOLO video analytics
- Stores alarm hash on Ethereum using iOS device UUID
- Triggers Web3 payment for emergency services via AgentKit

Why AgentKit?
- Seamless Web3 interactions: AI agents handle on-chain transactions natively without users needing to interact with wallets.
- Decentralized service orchestration: Autonomous agents manage service bookings, payments, and user verification on Ethereum.
- Improved accessibility: ElderEase makes crypto-based payments easy for seniors, leveraging voice commands and AI automation.
- Future-Proofing: AgentKit’s framework scales with new Web3 protocols, allowing us to integrate EigenLayer AVSs, IPFS storage, and libp2p P2P networking.

Qualification Requirements & Compliance

🔹 Built with AgentKit in a meaningful way: We use AgentKit for wallet integration, on-chain transactions, and AI-agent payments.
 
 🔹 AI Agents interacting with Ethereum: Our AI concierge executes Web3 payments, verifies service completion, and interacts with smart contracts autonomously.
 
 🔹 User-friendly and decentralized: ElderEase provides an intuitive interface (Alexa Skills & mobile app) while ensuring all transactions are trustless and verifiable.

ElderEase is bringing Web3 to everyday elderly care services—powered by AI, AgentKit, and Ethereum. 🚀

