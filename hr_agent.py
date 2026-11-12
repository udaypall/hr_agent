
import asyncio
import os

from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Load environment variables
load_dotenv()

# Check API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env file")


async def main():

    # Get user inputs
    job_role = input("Enter your desired job role: ")
    skill_set = input("Enter your skill set (comma separated): ")

    # Create OpenAI model client
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini"
    )

    try:
        # Create HR Assistant Agent
        hr_agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant."
        )

        # Dynamic task
        task = f"""
Create a job description based on the following details:

Job Role: {job_role}
Skill Set: {skill_set}

Instructions:
1. Generate exactly five points, numbered 1 to 5.
2. Each point must be written on a single line.
3. Do not use sub-points or additional line breaks.
4. Make every point relevant to the given job role and skill set.
5. Include relevant responsibilities and technical expectations.
6. Do not include a heading, introduction, or conclusion.

Output format:
1. First point
2. Second point
3. Third point
4. Fourth point
5. Fifth point
"""

        # Run agent and display response
        await Console(
            hr_agent.run_stream(task=task)
        )

    finally:
        # Close model client
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
