# URL Shortener

This is a simple Python script that uses the `pyshorteners` library to shorten URLs. It takes long URL as input and generates a shorter, more manageable URL that can be easily shared with others.

## Installation

To use this script, you'll need to have Python 3 installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

You'll also need to install the `pyshorteners` library. You can do this using pip, the Python package manager, by running the following command:

```
pip install pyshorteners
```

## Usage

To use the script, simply run it from the command line and enter the URL you want to shorten when prompted:

```
python url_shortener.py
Enter the URL: https://www.example.com/this-is-a-really-long-url-that-i-want-to-shorten
```

The script will then generate a shortened URL using the `tinyurl` method of the `Shortener` class and print it to the console:

```
https://tinyurl.com/yx9z5z8c
```

You can then copy and share this URL with others.

## Contributing

If you find a bug or have a suggestion for how to improve this script, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This script was inspired by the [pyshorteners documentation](https://pyshorteners.readthedocs.io/en/latest/).
