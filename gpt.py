import os
import openai

openai.api_key = os.environ['OPENAI_KEY']


def generate_text(prompt):

  response = openai.Completion.create(engine="text-davinci-003",
                                      prompt=prompt,
                                      temperature=0.9,
                                      max_tokens=4000,
                                      top_p=1.0,
                                      frequency_penalty=0.5,
                                      presence_penalty=0.0)

  return response['choices'][0]['text']
