# YouTube Video Summarizer

This project is a powerful YouTube Video Summarizer that can process any YouTube video and provide a concise summary of its content. The application uses advanced AI techniques to transcribe and summarize videos, whether they have captions or not. The summary is presented in 1-2 well-structured paragraphs for easy reading.

## Features

- Works with ANY YouTube video, with or without captions
- Multiple transcription methods:
  - Native YouTube captions (fastest)
  - Auto-translated captions from other languages
  - AI-powered audio transcription for videos without captions
- Smart summarization using state-of-the-art language models
- Easy-to-use command-line interface

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

## Prerequisites

1. Python 3.6 or higher
2. FFmpeg (required for audio processing)
   - Windows: Install using [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/): `winget install -e --id Gyan.FFmpeg`
   - Mac: Install using Homebrew: `brew install ffmpeg`
   - Linux: Install using package manager: `sudo apt install ffmpeg` (Ubuntu) or equivalent

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

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Enter a YouTube video URL when prompted. The application supports various URL formats:
   ```
   https://www.youtube.com/watch?v=VIDEO_ID
   https://youtu.be/VIDEO_ID
   ```

3. Wait while the application:
   - Attempts to fetch YouTube captions
   - If no captions are available, downloads and transcribes the audio
   - Generates a concise summary

4. Read the generated summary, which will be displayed in the console.

Note: The first time you process a video without captions, the application will download the Whisper model (about 150MB). This is a one-time process.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
=======
# Youtube-Transcript-Summarizer
>>>>>>> 64242b3ea66bf89bf5f9fd9b05c81a0f65918270
