# Hugging Face and LLM Post Generation

This project leverages the power of Hugging Face's language models to generate high-quality content for social media posts. The application is designed to assist users in creating engaging and informative content for their threads, including titles, keywords, and the posts themselves.

## Features

* **Title Generation**: Users can input a topic and generate a list of 10 creative and attention-grabbing title options for their post.
* **Keywords Generation**: Based on the title, the application generates a set of 5 keywords that can be used to optimize the post for search engines and improve its discoverability.
* **Post Generation**: Using the title and keywords, the application generates a high-quality, informative, and plagiarism-free social media post. The content is structured into introduction, body paragraphs, and a conclusion with a call-to-action (CTA). The post is designed to be engaging, conversational, and optimized for a beginner audience and tech enthusiasts.

## Technical Details

* The application utilizes Streamlit for its user interface, making it easy to use and interactive.
* The content generation is powered by Hugging Face's language models, specifically the Mistral-Nemo-Instruct-2407 model.
* The application uses environment variables to store the API key for Hugging Face, ensuring secure access to the language models.
* The project includes a `.gitignore` file to exclude unnecessary directories and files from version control.

## Getting Started

To use this application, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment using `python -m venv .venv`
3. Activate your environment to install locally the dependencies.
4. Create a `.env` file in the root directory of the project and add the `API_KEY` variable with your Hugging Face API key. You can use the `.env.example` file as a template.
5. Install the required dependencies using `pip install -r requirements.txt`.
6. Run the application using `streamlit run app.py`.
7. Follow the prompts in the application to generate titles, keywords, and posts for your social media threads.

## Contributing

Contributions to this project are welcome. If you have any suggestions or improvements, please submit a pull request.
