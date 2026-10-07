import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load environment variables from .env file
load_dotenv()

# 2. Initialize the Gemini Chat Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.7
)

# 3. Create a Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and concise AI assistant."),
    ("human", "Tell me a fun fact about {topic}.")
])

# 4. Set up an Output Parser
output_parser = StrOutputParser()

# 5. Create the LCEL Chain
chain = prompt | llm | output_parser

# 6. Run the chain
if __name__ == "__main__":
    user_topic = "quantum computing"
    print(f"Generating a fun fact about {user_topic}...\n")
    
    response = chain.invoke({"topic": user_topic})
    print(response)