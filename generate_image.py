import openai
import requests
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_response = requests.get(image_url)
    image_data = BytesIO(image_response.content)
    return image_data


if __name__ == '__main__':
    filename = 'generated_image.jpg'
    i = 1
    while os.path.isfile(filename):
        # File already exists, add suffix to filename
        i += 1
        filename = f"generated_image_{i:03d}.jpg"
    image_data = generate_image('(RAW photo, ((vector illustration)) of of window from the inside of house looking outside at the rain, couch in front of window, end table next to couch, lamp on end-table) 8k uhd,  vector, line drawing, line art, ((white background, black lines))')
    with open(filename, 'wb') as f:
        f.write(image_data.read())
