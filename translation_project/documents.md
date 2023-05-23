
# Django REST API for Translation

This Django REST API project allows users to translate words, phrases, or paragraphs using the Google Translate API. The API supports configuring the source and target languages via query parameters and provides translated results as responses.

## Features

- Translate words, phrases, or paragraphs using the Google Translate API.
- Configure source and target languages via query parameters.
- Caching mechanism to store and serve translated data to optimize performance.
- Utilizes Django's ORM for storing translations in a database.
- API endpoints are implemented using Django Rest Framework.

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```shell
   cd translation_project
   ```

3. Create a virtual environment (optional):

   ```shell
   python -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the Django development server:

   ```shell
   python manage.py runserver
   ```

## API Endpoints

### Translate Text

**Endpoint:** `/translate/`

**Method:** GET

**Parameters:**
- `text` (required): The text to be translated.
- `target_language` (required): The target language for translation.
- `source_language` (optional): The source language of the text. Defaults to 'auto' if not provided.

**Response:**
- If successful, returns a JSON response with the translated text.
- If an error occurs, returns a JSON response with an error message.

### Example Usage

**Request:**
```
GET /translate/?text=Hello&target_language=es&source_language=en
```

**Response:**
```json
{
  "translation": "Hola"
}
```

## Caching and Database Storage

To optimize performance, the API incorporates a caching mechanism using Django's caching framework. Translated data is cached to reduce the number of external API calls. If a user requests data that has already been translated, it is served from the cache.

Additionally, translated data is stored in a database using a `Translation` model. The model includes fields to store the original text, target language, source language, and translated text. This allows efficient retrieval of translations from the database.

## Testing

The project includes test cases to ensure the correctness and functionality of the API. The tests cover different scenarios, including translation requests, caching, and database operations. The `unittest` library is used for writing and executing the tests.

To run the tests, execute the following command:

```shell
python manage.py test
```

## Conclusion

The Django REST API for translation provides a convenient way to translate text using the Google Translate API. It offers flexibility in configuring the source and target languages, includes caching and database storage for efficient retrieval of translated data, and has comprehensive test coverage. The API can be easily integrated into other applications or used as a standalone service.

Please refer to the project's documentation for more details on the available endpoints, configurations, and customization options.

---

Feel free to customize and expand upon this markdown file to provide a more detailed description and explanation of your specific Django REST API for translation.