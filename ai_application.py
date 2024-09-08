"""
Create langchings and expose it for import.
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("API_KEY")

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-Nemo-Instruct-2407',
    token=api_key,
    temperature=0.7
)

promp_template_title_suggestion = PromptTemplate(
    input_variables=['topic'],
    template= '''
        I'm planing a blog post on topic: {topic}.
        The title is informative, or humorous, or persuasive.
        The target audience is beginners, tech enthuasisats.
        Suggest a list of ten creative and attention-grabbing titles for this blog post.
        Don't give any explanation or overview to each title.
        format: list of titles.
        example output:
            1.Title one
            2.Title two
            3.Title three
    '''
)

prompt_template_for_post = PromptTemplate(
    input_variables=['title', 'keywords', 'number_of_posts'],  # Specify input variables
    template=  # Define the prompt template
    '''Write a high-quality, informative, and plagiarism-free social media post on the topic: "{title}". 
    Target the content towards a beginner audience and tech. 
    Use a conversational writing style and structure the content with an introduction, 
    body paragraphs, and a conclusion with a CTA. 
    Try to split the content into {number_of_posts} number of posts. 
    Aim for a post length of 500 characters. 
    Try to incorporate these keywords: {keywords}
    Make the content engaging and capture the reader's attention.
    Use emojis and only one hashtag for each post.
    format: unicode
    '''
)

prompt_template_for_keywords = PromptTemplate(
    input_variables=['num_of_keywords', 'topic'],
    template='Write {num_of_keywords} keywords for a Threads post about {topic}'
)

title_chain = promp_template_title_suggestion | llm
post_chain = prompt_template_for_post | llm
keywords_chain = prompt_template_for_keywords | llm
