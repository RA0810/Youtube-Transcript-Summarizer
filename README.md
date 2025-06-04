# README.md

# YouTube Transcript Summarizer

This project is a YouTube Transcript Summarizer that allows users to input a YouTube video URL and receive a concise summary of the video's content. The application utilizes natural language processing techniques to transcribe and summarize the video transcript into 1-2 paragraphs, each consisting of 3-4 lines.

## Features

- Fetches video transcripts from YouTube.
- Summarizes transcripts into concise summaries.
- User-friendly web interface for inputting YouTube URLs.

## Project Structure

```
youtube-summarizer
├── src
│   ├── main.py          # Entry point of the application
│   ├── transcriber.py    # Handles transcript fetching
│   ├── summarizer.py     # Handles summarization logic
│   ├── utils.py          # Utility functions
│   └── templates
│       ├── index.html    # Input page template
│       └── summary.html   # Summary output template
├── requirements.txt      # Required libraries and dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── tests
    ├── __init__.py      # Marks tests directory as a package
    ├── test_transcriber.py # Unit tests for Transcriber
    └── test_summarizer.py  # Unit tests for Summarizer
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-summarizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables in the `.env` file as needed.

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the YouTube video URL and submit to receive the summary.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.