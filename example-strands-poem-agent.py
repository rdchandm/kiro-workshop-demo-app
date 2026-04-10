from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import http_request

SYSTEM_PROMPT = """
You are a helpful agent that writes poems.
If the user asks for a poem on a topic, write a poem on that topic. If the user gives you a web link you should use that
to look up information to use in the poem.
If asked for a short poem keep it under 50 words.
If the user asks for anything else, tell them you can only write poems.
""".strip()


@tool
def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())

# Bedrock
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    temperature=0.3,
)

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=[word_count, http_request],
    model=bedrock_model,
)

if __name__ == "__main__":
    print("Poem Agent - Enter 'quit' to exit")
    print("-" * 50)

    while True:
        # Example input "Write a short poem about Kiro autonomous agent based on the information on https://kiro.dev/autonomous-agent/"
        user_prompt = input("\nWhat would you like a poem about?")

        if user_prompt.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break

        response = agent(user_prompt)
        print(f"\n\n{response.message}\n\n")
