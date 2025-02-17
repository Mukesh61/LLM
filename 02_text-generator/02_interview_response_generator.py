'''
This example is more like a guided one as compare to previos one. 
'''
from transformers import pipeline

text_gen_pipe = pipeline(task='text-generation', model='distilgpt2')

input_promt = 'Thanks for this opportunity. I got to learn something new about Pyspark today.'

response = 'Thank you !'

promt_msg = f'''Interview Experience of candidate: 
{input_promt} 
Interviewer response:
{response}
'''

prompt_response = text_gen_pipe(promt_msg, max_length = 70, pad_token_id=text_gen_pipe.tokenizer.eos_token_id)

print(prompt_response)
