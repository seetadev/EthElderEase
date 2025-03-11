# Eth ElderEase
ElderEase is an AI-powered concierge that leverages Amazon Bedrock, AgentKit, Storacha, Js-libp2p and Nethermind (dotnet-libp2p), EigenLayer AVS to provide secure, decentralized home assistance and emergency monitoring for seniors.

🧩 Tech Stack & Architecture

1️⃣ AI-Powered Concierge & Automation (Amazon Bedrock + LLMs)
- Amazon Bedrock Agents power ElderEase’s concierge, handling service requests, scheduling, and real-time decision-making.
- Uses RAG (Retrieval-Augmented Generation) with Amazon Knowledge Bases to provide personalized responses based on elderly users' preferences, past interactions, and care needs.
- Custom fine-tuned LLMs run on Bedrock, trained on elder care best practices, home maintenance data, and emergency protocols.
- Dynamic AI workflows: Using Amazon Bedrock’s orchestration capabilities, we created "chain-of-thought" workflows, allowing AI agents to reason step-by-step before taking action.

2️⃣ Web3 Payments & Smart Contracts (AgentKit + Ethereum + Filecoin)
- AgentKit enables seamless, gas-efficient payments for services via FIL, ETH, or stablecoins.
- Smart contract escrow system ensures that payments are held until AI agents verify service completion.
- Uses EigenLayer AVS (Hyperlane, Gaia) for trustless verification of completed tasks before releasing payments.
- Voice-Activated Web3 Payments: We connected Alexa Skills to AgentKit, enabling seniors to pay service providers with "Alexa, confirm my home cleaning payment."

3️⃣ Peer to Peer Communication between AI agents using Storacha backend
  Secure & P2P AI Communication JS-libp2p and Nethermind’s dotnet libp2p
- AI agents communicate directly using libp2p’s P2P networking stack instead of relying on centralized APIs.
- Enables secure, low-latency service coordination between caregivers, cleaning staff, and maintenance teams.
- No Centralized API Calls: Using Nethermind’s dotnet libp2p, AI agents send service requests, confirm payments, and exchange status updates without ever touching centralized cloud APIs.

4️⃣ AI-Powered Computer Vision & Emergency Alerts (FFmpeg + TinyYOLO + IPFS + Ethereum)
ElderEase’s home monitoring system uses cameras (ONVIF, RTSP, HTTP, iOS) with FFmpeg and TinyYOLO AI models to detect:
 -  Falls or accidents
 -  Intruders or unexpected movement
 -  Leaking pipes, fire hazards, or broken appliances

If a critical event is detected, AI agents generate an alert, which is:
- Saved on IPFS
- Hashed and stored on Ethereum using the iOS device UUID as the lookup key
- Broadcasted via EigenLayer AVS (Witness Chain) for decentralized verification

No Cloud Storage Needed: Instead of relying on AWS or Google Cloud for event logs, ElderEase stores alarms directly on IPFS, ensuring privacy and censorship resistance.

5️⃣ EigenLayer AVS for On-Chain Verification (Hyperlane + Gaia + Opacity)
ElderEase integrates EigenLayer AVSs for decentralized verification of services and alarms:
 -  Hyperlane: Verifies service execution across chains
 -  Gaia: Ensures AI-generated alerts are verifiable and tamper-proof
 -  Opacity: Provides on-chain privacy for AI transactions
Hacky Trick:
 🔹 EigenLayer AVS as AI Validators: We use Gaia AVS to verify object detection results—ensuring that AI doesn’t falsely trigger alerts due to hallucinations.

6️⃣ Scalable AI Knowledge Base on AWS (S3 + Bedrock + EC2 Hosting)
AI concierge retrieves personalized recommendations from an S3-hosted knowledge base.
EC2 instances host AI-driven home cleaning services, scaling as demand grows.
Hacky Trick:
 🔹 Custom LLM Indexing: Instead of using a single vector DB, we precompute and cache embeddings for faster responses.

🚀 Key Innovations & Why It’s Exciting
 
 AI concierge that combines Bedrock AI + AgentKit Web3 Payments + P2P Networking
 - EigenLayer AVSs for verifiable, trustless service execution
 - Decentralized, AI-driven emergency alerts stored on IPFS
 - Privacy-first, Web3-powered elderly care that removes the need for centralized platforms
ElderEase isn’t just an AI concierge—it’s a fully autonomous Web3 elder care solution that blends AI, blockchain, and decentralized infrastructure into a seamless experience. 🚀

