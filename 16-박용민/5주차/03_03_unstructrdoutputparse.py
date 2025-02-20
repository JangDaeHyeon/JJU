# -*- coding: utf-8 -*-
"""03-03_UnstructrdOutputparse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b5pdmbvTen8MMx4CoThlrbrrKJvZv0tY
"""

import os

os.environ["OPENAI_API_KEY"] = "api-key"
os.environ["LANGCHAIN_API_KEY"] = "api-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "http://api.smith.langchain.com"
os.environ["LANGCHAINPROJECT"] = "03-02-03"

!pip install langchain_openai

from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


response_schema = [
    ResponseSchema(name='answer', description='사용자의 질문에 대한 답변'),
    ResponseSchema(name='source', description="사용자의 질문에 대한 출처는 어디인지")
]

# StructuredOutputParser 생성
output_parser = StructuredOutputParser.from_response_schemas(response_schema)

# 올바른 메서드 호출
format_instruction = output_parser.get_format_instructions()

# PromptTemplate 정의
prompt = PromptTemplate(
    template="""answer the user's questions as best as possible.
{format_instructions}
{question}""",
    input_variables=['question'],  # input_variables 수정
    partial_variables={"format_instructions": format_instruction},
)

model = ChatOpenAI(temperature=0, model = 'gpt-4o')

type(response_schema)

chain = prompt | model | output_parser

response = chain.invoke({"question": "What is the capital of France?"})
response