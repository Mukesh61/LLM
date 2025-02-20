from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm_gpt_model = ChatOpenAI(model="gpt-4o-mini", api_key='<give your open ai token here>')		

prompt_template_data = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and a Guru."),
        ("human", "Respond to question: {question}")
    ]
)

llm_lang_chain = prompt_template | llm
response = llm_lang_chain.invoke({"question": "Best way to learn and retain knowledgen?"})
print(response.content)


'''
Tips to retaining learning effectively

1. Active Engagement: Engage with the material actively rather than passively reading or listening. Take notes, summarize concepts in your own words, and teach the material to someone else.

2. Spaced Repetition: Use spaced repetition techniques to review material at increasing intervals over time. This helps reinforce memory and prevents forgetting.

3. Practice Retrieval: Regularly test yourself on the material you have learned. Use flashcards, quizzes, or practice tests to reinforce your knowledge.

4. Connect to Prior Knowledge: Relate new information to what you already know. Making connections helps deepen understanding and enhances retention.

5. Utilize Multiple Learning Modalities: Engage different senses and methods of learning. Use visual aids, listen to podcasts, or watch videos related to the topic.

6. Break Information into Chunks: Divide material into smaller, manageable pieces. This makes it easier to process and remember.

7. Stay Organized: Keep your notes, resources, and information organized. Review your organization regularly to help reinforce learning.

8. Create Mnemonics: Use mnemonic devices, acronyms, or visual imagery to help remember complex information.

9. Stay Curious: Cultivate a genuine interest in the material. When you care about what you're learning, you’re more likely to remember it.

10. Regular Review: Set aside time to regularly review what you’ve learned. Frequent review sessions can significantly improve retention.

11. Healthy Lifestyle: Ensure you maintain a balanced diet, get enough sleep, and exercise regularly. These factors significantly impact cognitive function and memory.

12. Mindfulness and Focus: During your study sessions, minimize distractions and practice mindfulness to improve concentration and retention.

'''
