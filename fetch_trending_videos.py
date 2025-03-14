import json
import os


def generate_ideas_from_trending():
    trending_videos = fetch_trending_videos()  # ✅ Correct function call

    if not trending_videos:
        return ["❌ No trending videos found!"]

    # Generate content ideas based on trending video titles
    content_ideas = [f"Idea: {title} - Create a unique take on this topic!" for title in trending_videos]

    return content_ideas

def save_ideas():
    ideas = generate_ideas_from_trending()

    if ideas:
        with open("content_ideas.json", "w", encoding="utf-8") as file:
            json.dump(ideas, file, indent=4, ensure_ascii=False)
        print("✅ Content ideas saved successfully!")
        print("📂 File path:", os.path.abspath("content_ideas.json"))
    else:
        print("⚠️ No ideas generated.")

if __name__ == "__main__":
    save_ideas()
