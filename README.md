# captcha_test_3

## Overview

`captcha_test_3` is a simple web application that solves CAPTCHAs by processing image URLs provided as query parameters. The application defaults to a sample CAPTCHA image if no URL is provided.

## Features
- Displays CAPTCHA image from a provided URL.
- Solves the CAPTCHA and displays the solved text within 15 seconds.
- Default to a sample CAPTCHA image if no URL is specified.
- Supports handling of SVG images in addition to PNG and other formats.
- Supports audio CAPTCHA formats for enhanced accessibility.
- User registration and login functionality with a database.
- User profile management to update necessary information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/captcha_test_3.git
   cd captcha_test_3
   ```

2. Install the required packages:
   ```bash
   pip install Flask Pillow pytesseract Flask-SQLAlchemy Werkzeug
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/?url=<your_image_url>`.

## Usage

To use the application, simply provide a URL to a CAPTCHA image as a query parameter. For example:
```
http://127.0.0.1:5000/?url=https://example.com/captcha.png
```
If no URL is provided, the application will use a default sample CAPTCHA image.

You can also use SVG images by providing a URL to an SVG file:
```
http://127.0.0.1:5000/?url=https://example.com/captcha.svg
```

Additionally, the application now supports audio CAPTCHA formats. You can provide a URL to an audio CAPTCHA file:
```
http://127.0.0.1:5000/?url=https://example.com/captcha.mp3
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.