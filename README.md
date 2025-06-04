# Financial Q&A API

A simple REST API that answers personal finance questions using an open-source AI model (distilgpt2). 
The project uses FastAPI and is lightweight, fast, and easy to run anywhere.

## How to Run 

### Option 1: Run Locally with Python 

1. Install requirements:
   ```
   pip install fastapi uvicorn transformers nest-asyncio
   ```
2. Start the API:
   ```
   uvicorn main:app --reload
   ```
3. 
-Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser and test!
-When testing the API in "/docs", replace the example question with your actual question.


## Option 2: How to Run with Docker

Note: Make sure you have Docker Desktop installed

1. Create a file named Dockerfile (no extension!) in the same folder as your main.py file, with the following content:
   ```
   FROM python:3.11-slim

   WORKDIR /app

   COPY requirements.txt .

   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8000

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

   ```
2. Open PowerShell or Terminal in your project folder and run: 
   ```
   docker build -t finance-ai-api .
   ```
3. Run the Docker container:
   ```
   docker run -p 8000:8000 finance-ai-api
   ```
4. Open your browser and go to [http://127.0.0.1:8000/docs] to test the API.

## Running with Docker:
- Make sure you have a file named Dockerfile , without extension, in your project folder

## How to test the API: 


- In the page that will open click on the "default" and then click on the "Try it out" button 

- Delete the example question and add your finance question and then click on the blue button "Execute" 

- Scroll down to see the answer on the Response body.

- Delete your previous question and add the new one if you want. 


## Why I picked distilgpt2

- It is open-source, lightweight, and runs easily on any computer in a Docker container.
- It gives simple, fast answers ideal for prototyping.
- Easy to add guardrails for safety.

## Sample Questions

{ "question": "How do I start budgeting?" }
{ "question": "What is an emergency fund?" }
{ "question": "How does compound interest work?" }
{ "question": "What is the difference between a credit card and a debit card?" }

##  Requirements
-fastapi
-uvicorn
-transformers
-torch






