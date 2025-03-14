import google.generativeai as genai
import os
from fetch_trending import fetch_trending_videos

# ✅ Secure API Key Setup
GEMINI_API_KEY = os.getenv("AIzaSyBJXsWyhtpUek24cgRsyZhrqH0PegjNBs")
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use the correct model (Change if needed)
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_ideas_from_trending():
    trending_videos = fetch_trending_videos()
    if not trending_videos:
        return ["❌ No trending videos found."]

    prompt = f"""
    You are an AI expert in YouTube content creation. Based on these trending YouTube videos:
    {trending_videos}

    Suggest **5 highly creative and unique video ideas** with detailed descriptions.
    """

    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text.strip().split("\n")
        else:
            return ["❌ No ideas generated."]

    except Exception as e:
        return [f"❌ Error: {str(e)}"]

if __name__ == "__main__":
    print("💡 AI-Generated Video Ideas from Trending Topics:")
    for idea in generate_ideas_from_trending():
        print(f"✅ {idea}")
