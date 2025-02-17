from transformers import pipeline

sumarizer_pipe = pipeline(task='summarization', model='facebook/bart-large-cnn')

data = 'give story of Cinderella'

summary = sumarizer_pipe(data, max_length = 60)

print(summary)
