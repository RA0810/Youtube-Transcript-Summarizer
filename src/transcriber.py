from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class Transcriber:
    def fetch_transcript(self, youtube_url):
        """Fetch and concatenate transcript text from a YouTube video."""
        try:
            video_id = self._extract_video_id(youtube_url)
            try:
                # Try getting transcript directly first
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                if transcript:
                    return " ".join(item['text'] for item in transcript)
            except Exception as e:
                try:
                    # If direct fetch fails, try getting all available transcripts
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    
                    # Try auto-translated English if available
                    try:
                        transcript = transcript_list.find_generated_transcript(['en'])
                    except:
                        # Try other languages and translate to English
                        languages = transcript_list.get_language_codes()
                        if languages:
                            transcript = transcript_list.find_transcript(languages[:1])
                            print(f"Found transcript in {transcript.language}. Translating to English...")
                            transcript = transcript.translate('en')
                        else:
                            print("No transcripts available for this video.")
                            return None
                    
                    transcript_data = transcript.fetch()
                    return " ".join(item['text'] for item in transcript_data)
                    
                except Exception as inner_e:
                    print(f"\nError: Could not find or translate transcripts.")
                    print("Please try a video with English captions available.")
                    return None
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
            print("Please use a complete YouTube URL like:")
            print("- https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("- https://youtu.be/dQw4w9WgXcQ")
            return None
    
    def _extract_video_id(self, youtube_url):
        """Extract video ID from various YouTube URL formats."""
        try:
            # Remove any query parameters after '?si='
            url = youtube_url.split('?si=')[0]
            query = urlparse(url)
            if query.hostname == 'youtu.be':
                return query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    return parse_qs(query.query)['v'][0]
            raise ValueError("Could not extract video ID from URL")
        except:
            raise ValueError("Invalid YouTube URL format")