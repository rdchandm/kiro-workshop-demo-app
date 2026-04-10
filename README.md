# Strands Poem Agent

An interactive AI agent that writes poems using [Strands Agents](https://strandsagents.com/) and Amazon Bedrock.

The agent can write poems on any topic. If you provide a web link, it will fetch information from that URL and use it as inspiration for the poem.

## Prerequisites

- Python 3.10 or later
- AWS credentials configured with access to Amazon Bedrock (the agent uses the `us.amazon.nova-2-lite-v1:0` model)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/rdchandm/kiro-workshop-demo-app.git
   cd kiro-workshop-demo-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the agent:

```bash
python example-strands-poem-agent.py
```

You will be prompted to enter a topic. For example:

```
Write a short poem about Kiro autonomous agent based on the information on https://kiro.dev/autonomous-agent/
```

Type `quit`, `exit`, or `q` to stop the agent.
