#!/usr/bin/env python
# coding: utf-8

# # **Finance - Ai - API**

# The app will be created using an open source language model from Hugging face. I decided to work with "distilgpt2" because of its lightweight and runs easily in any computer. Also, it gives simple and fast answers. However, in some cases the content of the asnwers can be offensive, so i will put some guardrails to keep it safe. The model gives quick and straightforward answers to personal finance questions.

# In[1]:


#install necessary packages
# !pip install fastapi uvicorn nest-asyncio transformers 


# In[2]:


from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline

app = FastAPI()

generator = pipeline("text-generation", model="distilgpt2")

class Question(BaseModel):
    question: str = Field(
        example="How can I start budgeting?"
    )
        
def is_question_safe(question:str) -> bool:
    bad_words = ["kill","stupid", "suicide","hack","cheat"]
    lowered = question.lower()
    return not any(word in lowered for word in bad_words)

def is_answer_safe(answer:str) -> bool:
    lowered = answer.lower()
    return not any(word in lowered for word in bad_words)

@app.post("/ask")
def ask_question(q: Question):
    if not is_question_safe(q.question):
        return {"answer": "Sorry, i can't answer to this question. Please ask a safe and appropriate finance question."}
    prompt = f"Q: {q.question}\nA:"
    result = generator(prompt, max_length=100, num_return_sequences=1)
    answer = result[0]['generated_text'][len(prompt):]
    if not is_answer_safe(answer):
        return {"answer": "Sorry, I can't provide an answer to that question."}
    return {"answer": answer}


# In[3]:


#import nest_asyncio in order to run asynchronous code inside environments that already have a running event loop
#without it, the uvicorn will crash out
import nest_asyncio
nest_asyncio.apply()


# - Start the server: "uvicorn main:app --reload"
# 
# - Copy the link below and paste it in your browser: http://127.0.0.1:8000/docs
# 
# - In the page that will open click on the "default" and then click on the "Try it out" button 
# 
# - Delete the example question and add your finance question and then click on the blue button "Execute" 
# 
# - Scroll down to see the answer on the Response body.
# 
# - Delete your previous question and add the new one if you want. 

# In[ ]:


import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)


# In[20]:


# http://127.0.0.1:8000/docs

