
# URL Shortener 🔗

A simple URL Shortener web application built using **Python Flask and SQLite**.

This project converts a long URL into a short URL. The original URL and generated short code are stored in a database. When the short URL is opened, the user is redirected to the original URL.

## Features

- Shorten long URLs
- Generate unique short codes
- Store URLs in SQLite database
- Redirect short URLs to original URLs
- Handle duplicate URLs
- Simple and user-friendly interface

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS

## Project Structure

```text
URL-Shorter-python/
│
├── URL_shorter.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    └── result.html
````

## How It Works

1. Enter a long URL.
2. Click the **Shorten URL** button.
3. The application generates a unique short code.
4. The URL and short code are stored in SQLite.
5. The generated short URL is displayed.
6. Opening the short URL redirects to the original URL.

## Example

**Original URL:**

```text
https://www.google.com
```

**Generated Short URL:**

```text
http://127.0.0.1:5000/Ab12Xy
```

## Database

The project uses SQLite to store URL information.

### URL Table

| Field        | Description          |
| ------------ | -------------------- |
| id           | Unique ID            |
| original_url | Original long URL    |
| short_code   | Generated short code |

## Installation

Clone the repository:

```bash
git clone https://github.com/saniya2698/URL-Shorter-python.git
```

Open the project folder:

```bash
cd URL-Shorter-python
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python URL_shorter.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Testing

The application was tested for:

* Valid URL input
* Empty URL input
* URL shortening
* Duplicate URLs
* Short URL redirection
* Database storage
* Invalid short codes
* Multiple URLs

## Future Enhancements

* User login and registration
* Custom short URLs
* URL expiration
* Click tracking
* QR code generation
* User dashboard
* Cloud deployment

## Learning Outcomes

This project helped me understand:

* Flask application development
* Flask routing
* HTML form handling
* SQLite database integration
* SQLAlchemy
* URL redirection
* Git and GitHub

## Author

**Saniya Shaikh**

GitHub: [saniya2698](https://github.com/saniya2698)

## License

This project was created for educational and practical learning purposes.

````

