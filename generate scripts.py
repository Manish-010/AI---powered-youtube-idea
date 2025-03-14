import google.generativeai as genai

# Set up Gemini API key
GEMINI_API_KEY = "AIzaSyBJXsWyhtpUek24cgRsyZhrqH0PegjNBsg"  # Replace with your valid API key
genai.configure(api_key=GEMINI_API_KEY)


# noinspection PyShadowingNames
def generate_script(topic):
    """Generate a full YouTube video script based on a given topic."""
    prompt = f"""
    Generate a detailed, engaging YouTube video script about "{topic}".
    The script should include:
    - A catchy **Introduction**
    - Key **discussion points** (with clear headings)
    - A smooth **Conclusion**
    - A call-to-action (CTA) for engagement.

    Ensure the script flows naturally and is engaging for viewers.
    """

    model = genai.GenerativeModel("gemini-1.5-pro")  # Updated model name

    response = model.generate_content(prompt)

    return response.text.strip() if response else "⚠️ Failed to generate script."


# Test the function (Optional)
if __name__ == "__main__":
    topic = "How AI is revolutionizing video editing"  # Example topic
    print("🎬 AI-Generated YouTube Video Script:")
    print(generate_script(topic))



