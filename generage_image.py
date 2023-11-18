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
    image_data = generate_image('A giant tree growing out of a cityscape, digital painting, cyberpunk, (modernist), Stanley Artgerm Lau, artstation, unreal engine, (vray), (expansive), low angle shot,')
    with open('generated_image.jpg', 'wb') as f:
        f.write(image_data.read())
