from scraper import fetch_website_contents
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""

def get_messages(content):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + content}
    ]

def get_content(url):
    return fetch_website_contents(url)

def get_llm_response(url):
    openai = OpenAI()
    content = get_content(url)
    messages = get_messages(content)
    llm_response = openai.chat.completions.create(model="gpt-5.2", messages=messages)
    return llm_response.choices[0].message.content


if __name__ == "__main__":
    print(get_llm_response("https://edwarddonner.com"))
