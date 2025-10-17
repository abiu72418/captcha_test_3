from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==')
    image = None

    if url.startswith('data:image/png;base64,'):
        image_data = url.split(',')[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
    elif url.endswith('.mp3') or url.endswith('.wav'):
        # Handle audio CAPTCHA formats (this is a placeholder for actual audio processing)
        return render_template('index.html', captcha_url=url, captcha_text='Audio CAPTCHA processing not implemented.')
    else:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

    captcha_text = pytesseract.image_to_string(image)
    return render_template('index.html', captcha_url=url, captcha_text=captcha_text)

if __name__ == '__main__':
    app.run(debug=True)