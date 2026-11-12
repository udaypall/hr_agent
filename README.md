# AutoGen HR Assistant Agent

## 1. Project Overview

This project demonstrates an AI-powered HR Assistant built using the **Microsoft AutoGen framework** and **OpenAI GPT-4o-mini**.

The agent dynamically generates a job description based on the job role and technical skills provided by the user.

Instead of using a fixed job title, users can enter any desired job role and relevant skill set.

## 2. Technologies Used

- Python
- Microsoft AutoGen AgentChat
- OpenAI GPT-4o-mini
- OpenAI API
- Asyncio
- python-dotenv

## 3. Project Structure

```text
hr_agent/
│
├── venv/
│
├── hr_agent.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 4. Features

- Creates an HR Assistant using AutoGen `AssistantAgent`.
- Uses the exact system message: `You are an HR assistant.`
- Integrates OpenAI GPT-4o-mini.
- Accepts dynamic job roles from users.
- Accepts multiple technical skills as input.
- Generates exactly five numbered points.
- Displays each point on a single line.
- Uses asynchronous execution with `asyncio`.
- Streams agent responses using AutoGen `Console`.
- Reads the OpenAI API key securely from environment variables.
- Closes the model client after execution.

## 5. Installation and Setup

### Step 1: Create Project Folder

```cmd
mkdir hr_agent
cd hr_agent
```

### Step 2: Create Virtual Environment

```cmd
python -m venv venv
```

### Step 3: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

### Step 4: Install Dependencies

```cmd
pip install -r requirements.txt
```

## 6. Environment Configuration

Create a `.env` file in the project directory.

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important:** Never upload your `.env` file or expose your API key on GitHub.

## 7. Run the Application

Execute the following command:

```cmd
python hr_agent.py
```

## 8. Example Execution

### User Input

```text
Enter your desired job role: AI Engineer

Enter your skill set (comma separated):
Python, LangChain, CrewAI, RAG, OpenAI API
```

### Expected Agent Output

```text
---------- TextMessage (hr_assistant) ----------

1. Develop AI-powered applications using Python and modern AI frameworks.
2. Build Retrieval-Augmented Generation pipelines using LangChain.
3. Design and implement multi-agent workflows using CrewAI.
4. Integrate OpenAI APIs into intelligent applications.
5. Optimize AI solutions for accuracy, performance, and scalability.
```

*Note: The actual generated descriptions may vary depending on the model response.*

## 9. Requirements

The project uses the following Python packages:

```text
autogen-agentchat
autogen-ext[openai]
python-dotenv
```

## 10. Learning Outcomes

Through this assignment, I learned:

1. How to create an AI Assistant Agent using Microsoft AutoGen.
2. How to configure OpenAIChatCompletionClient.
3. How to use system messages to define agent behaviour.
4. How to execute AutoGen agents using asyncio.
5. How to dynamically pass user inputs to an AI agent.
6. How to stream responses using AutoGen Console.
7. How to manage API keys using environment variables.

## 11. Future Enhancements

- Generate complete job descriptions with qualifications and experience.
- Export job descriptions into PDF or Word documents.
- Build a multi-agent recruitment workflow.
- Add a Streamlit-based HR Assistant interface.
- Integrate Google Sheets for storing job descriptions.

## 12. Author

**Project:** AutoGen HR Assistant Agent  
**Framework:** Microsoft AutoGen  
**Model:** OpenAI GPT-4o-mini  
**Language:** Python

---

*Assignment: Learn. Build. Operate.*