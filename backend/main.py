from glob import glob
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
import tensorflow as tf  
from pydantic import BaseModel 
from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering

class model_inputs(BaseModel) : 
    context : str 
    question : str





app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = TFAutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad",return_dict=False)

nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

origins =  ['http://localhost:3000'] 

app.add_middleware(
    CORSMiddleware , 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

@app.post('/predict/') 
async def predict(inputs : model_inputs) : 
    data = dict(inputs) 
    if model :
        question, context = data['question'] , data['context']
        result = nlp(question = question, context=context)
        return result['answer']
    return 'model has not loaded yet'


