# WitnessAI

> **Privacy-Preserving AI Digital Witness**  
> *Capture Facts. Reconstruct Events. Preserve Privacy.*

## 🚀 Live Demo

👉 **[Open WitnessAI Demo](https://witnessai-3q4namtae3nshyazy8pzii.streamlit.app/)**

## 📌 Project Overview

WitnessAI is an AI-assisted incident documentation system designed to help users capture, organize, and preserve factual information about incidents.

The system transforms a user's incident description into a structured record containing important facts, an event timeline, missing information, and user-verified details.

## ❗ Problem

During accidents, safety incidents, disputes, or other unexpected events, people may struggle to accurately remember and organize important details.

Important information such as:

- Time
- Location
- People involved
- Objects or vehicles
- Events and actions
- Sequence of events

can easily be missed or unclear.

## 💡 Solution

WitnessAI follows this workflow:

**Describe Incident → Extract Facts → Reconstruct Timeline → Identify Missing Information → Verify → Incident Record**

The system helps organize information without intentionally inventing facts.

## ✨ Key Features

- 🔍 **Fact Extraction** – Identifies time, location, people, objects, and events.
- 🕒 **Timeline Reconstruction** – Organizes described events chronologically.
- ❓ **Missing Information Detection** – Highlights important details that were not provided.
- ✅ **User Verification** – Allows users to review and verify the generated information.
- 🔒 **Privacy-Focused Design** – Designed to reduce unnecessary dependence on cloud-based processing.
- 🌐 **Simple Web Interface** – Built with Streamlit for easy access.

## 🧠 Technical Approach

### Current Prototype

- Python
- Streamlit
- Rule-based text processing
- Regular expressions
- Timeline processing

### Architecture

**User Input**  
↓  
**Streamlit Interface**  
↓  
**Python Processing Layer**  
↓  
**Fact Extraction + Timeline Engine**  
↓  
**Missing Information Detection**  
↓  
**User Verification**  
↓  
**Structured Incident Record**

## 📱 Example

Example incident description:

> "At around 7:30 PM, I was near the college gate. I saw a motorcycle hit a parked car. There were two people on the motorcycle. The driver stopped after the collision."

WitnessAI can identify information such as:

- **Time:** 7:30 PM
- **Location:** College / Gate
- **People:** Two people
- **Objects:** Motorcycle, Car
- **Events:** Hit, Collision
- **Timeline:** Events organized from the description
- **Missing Information:** Details that may require clarification

## 🔐 Privacy & Responsible AI

WitnessAI is designed around a privacy-first approach.

The system aims to:

- Keep sensitive information processing local where possible.
- Avoid unnecessary cloud dependence.
- Clearly distinguish provided information from missing information.
- Keep the user involved in verifying the generated record.
- Avoid presenting invented information as fact.

## ⚡ Snapdragon & Qualcomm AI Direction

WitnessAI is designed with future on-device AI deployment in mind.

The planned development direction includes:

- On-device AI inference
- Qualcomm AI Hub compatible models
- Snapdragon-powered PC optimization
- Local speech-to-text
- Advanced AI-based fact extraction
- Privacy-preserving local processing

**Note:** The current public prototype uses Python, Streamlit, and rule-based extraction. Snapdragon/Qualcomm AI Hub integration is the planned optimization direction and is not claimed as a completed integration in the current prototype.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web interface |
| Regular Expressions | Basic fact extraction |
| Rule-based NLP | Current text processing |
| Timeline Engine | Event organization |
| GitHub | Source code and version control |
| Streamlit Cloud | Public deployment |

## 📂 Project Structure

```text
WitnessAI/
│
├── app.py
├── ai_engine.py
├── timeline.py
├── requirements.txt
└── README.md
