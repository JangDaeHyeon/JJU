# -*- coding: utf-8 -*-
"""02.LCEL_241226_2_박용민.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H_N-CK5o5iAHk0hY5A-IFUpvkRfDD78f
"""

import os

api_key = ''

os.environ['OPENAI_API_KEY'] = api_key


from langchain_teddynote.messages import stream_response
from langchain_core.prompts import PromptTemplate

"""# 프롬프트 정의"""

template = "{country}의 수도는 어디인가요?"
prompt_template = PromptTemplate.from_template(template)
prompt_template

prompt = prompt_template.format(country = '대한민국')
prompt

prompt = prompt_template.format(country = '미국')
prompt

from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    max_tokens=2048,
    temperature=0.1,
)

model

prompt = PromptTemplate.from_template("(topic)에 대해 쉽게 설명해주세요.")

model = ChatOpenAI()

chain = prompt | model

prompt

input = {"topic": "인공지능 모델의 학습 원리"}
input

response = chain.invoke(input)
print(response)