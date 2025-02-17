from transformers import pipeline

translator_pipe = pipeline(task='translation_en_to_hi', model='Helsinki-NLP/opus-mt-en-hi')

input_promt = 'Hello, how are you.'

prompt_response = translator_pipe(input_promt, clean_up_tokenization_spaces=True )

print(prompt_response) # [{'translation_text': 'हैलो, तुम कैसे हो.'}]
