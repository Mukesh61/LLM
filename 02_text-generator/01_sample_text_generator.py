from transformers import pipeline

text_gen_pipe = pipeline(task='text-generation', model='distilgpt2')

input_promt = 'This is a story about Python programmer.'

response = text_gen_pipe(input_promt, max_length = 200, pad_token_id=text_gen_pipe.tokenizer.eos_token_id)
