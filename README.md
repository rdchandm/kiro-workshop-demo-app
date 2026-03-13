# Poem Agent

A poem-writing agent built with the [Strands Agents SDK](https://github.com/strands-agents/sdk-python) and powered by Amazon Bedrock. The agent uses the `us.amazon.nova-2-lite-v1:0` model to write poems on any topic. It can also follow web links to gather information and incorporate it into its poems.

## Prerequisites

- **Python 3.10+**
- **AWS credentials** configured with access to Amazon Bedrock. Your credentials must have permission to invoke the `us.amazon.nova-2-lite-v1:0` model. You can configure credentials using any standard method (environment variables, `~/.aws/credentials`, IAM role, etc.).

## Installation

Install the required dependencies:

```bash
pip install strands-agents strands-agents-tools
```

## Running the Agent

```bash
python example-strands-poem-agent.py
```

This starts an interactive CLI loop. Type a prompt to get a poem, or type `quit`, `exit`, or `q` to stop.

## Example Usage

```
Poem Agent - Enter 'quit' to exit
--------------------------------------------------

What would you like a poem about? Write a short poem about clouds

(the agent responds with a poem about clouds)

What would you like a poem about? Write a short poem about Kiro autonomous agent based on the information on https://kiro.dev/autonomous-agent/

(the agent fetches information from the URL and writes a poem)

What would you like a poem about? quit
Goodbye!
```

## How It Works

- A custom `word_count` tool lets the agent count words in text to stay within length constraints.
- The `http_request` tool from `strands-agents-tools` allows the agent to fetch content from URLs.
- The system prompt restricts the agent to only writing poems -- if you ask it to do something else, it will politely decline.
