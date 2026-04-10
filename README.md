# Poem Agent

An interactive CLI agent that writes poems on any topic. Built with the [Strands Agents SDK](https://github.com/strands-agents/sdk-python) and powered by Amazon Bedrock (Nova 2 Lite).

The agent can:
- Write poems on any topic you provide
- Fetch content from web links and use that information in poems
- Count words in generated text
- Keep poems short (under 50 words) when asked

## Prerequisites

- **Python 3.10+**
- **AWS account** with access to [Amazon Bedrock](https://aws.amazon.com/bedrock/) and the `us.amazon.nova-2-lite-v1:0` model enabled
- **AWS credentials** configured locally (via `aws configure`, environment variables, or an AWS credentials file)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rdchandm/kiro-workshop-demo-app.git
   cd kiro-workshop-demo-app
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install strands-agents strands-agents-tools
   ```

## Configuration

Make sure your AWS credentials are set up so the SDK can call Amazon Bedrock. The simplest approach is to export environment variables:

```bash
export AWS_ACCESS_KEY_ID=<your-access-key>
export AWS_SECRET_ACCESS_KEY=<your-secret-key>
export AWS_DEFAULT_REGION=us-east-1
```

Alternatively, run `aws configure` if you have the AWS CLI installed.

## Running the Agent

```bash
python example-strands-poem-agent.py
```

You will see an interactive prompt:

```
Poem Agent - Enter 'quit' to exit
--------------------------------------------------

What would you like a poem about?
```

Type a topic and press Enter. The agent will generate a poem and print it to the console. Type `quit`, `exit`, or `q` to stop.

## Example Usage

```
What would you like a poem about? Write a short poem about the ocean

  Waves whisper secrets to the shore,
  Salt and foam forevermore.
  Depths of blue stretch far and wide,
  Mysteries the currents hide.

What would you like a poem about? Write a short poem about Kiro based on https://kiro.dev/

  ...the agent fetches the page and writes a poem using that content...

What would you like a poem about? quit
Goodbye!
```
