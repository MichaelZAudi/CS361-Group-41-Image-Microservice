from flask import Flask, jsonify, request
from google import genai
from google.genai import types
from PIL import Image
import climage

client = genai.Client()

app = Flask(__name__)


# health check
@app.route('/health', methods = ['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200


@app.route('/image/prompt', methods = ['POST'])
def random_number():
    in_data = request.get_json()
    prompt = in_data.get('prompt')

    # no prompt, error
    if not prompt:
        return jsonify({'status': 'error',
                        'error_message': 'no valid prompt identified'}), 400

    # create an image from the prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
    )

    for part in response.parts:
        if part.text is not None:
            return jsonify({'status': 'error',
                            'error_message': part.text}), 400
        elif part.inline_data is not None:
            image = part.as_image()
            ret_image = climage.convert_pil(image, is_unicode=True)

    # success
    return jsonify({'status': 'success',
                    'return_value': ret_image}), 200
