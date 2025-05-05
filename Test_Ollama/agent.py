from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from scripts.regsetup import description

root_agent = Agent(
    name="root_agent",
    model=LiteLlm(model="ollama/llama3.2:latest"),
    description="agent to assist people",
    instruction="you are a helpful assistant."
)
