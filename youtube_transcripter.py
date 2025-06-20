import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Updated configuration for Mumbai, India
PROJECT_ID = 'neon-rex-453614-g1'
# 'AIzaSyA_EJIr4YJMnBXokQpKYiz4Enceeflp12U'  # Replace with your Google Cloud project ID
LOCATION = 'asia-south1'  # Mumbai region

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Initialize the vision model
vision_model = GenerativeModel("gemini-1.5-pro-001")

prompt = """
I have an hour-long video of a fitness coach performing a full workout routine. The video has no audio or subtitles, and I want to create a professional voiceover script to guide viewers through the session.

Please:
1. Analyze the video and break it down into segments (warm-up, main workout, cooldown, etc.).
2. For each exercise shown, identify the movement and provide:
   - The name of the exercise
   - Number of reps or duration (if estimable)
   - Clear and concise instructional narration in a motivational tone (e.g., "Keep your back straight", "Breathe in as you lower down").
3. Add transitions between exercises and segments (e.g., "Next up…", "Great job, let's move to the next set!").
4. Maintain a natural timing and pacing for an hour-long session.

The goal is to turn this silent video into a fully guided workout suitable for YouTube or a fitness app.
"""

# Note: YouTube URLs don't work directly - you need to upload video to Google Cloud Storage
# Replace with your Google Cloud Storage URI
video_uri = "gs://level_video_transcripter/FOR VO DAY 2.mp4"

try:
    # Generate content analysis
    response = vision_model.generate_content([
        Part.from_uri(video_uri, mime_type="video/mp4"),
        prompt,
    ])
    
    print("Generated Voiceover Script:")
    print("=" * 50)
    print(response.text)
    
except Exception as e:
    print(f"Error occurred: {e}")
    print("Make sure your video is uploaded to Google Cloud Storage and the URI is correct.")