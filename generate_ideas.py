from fetch_trending_videos import fetch_trending_videos


def generate_ideas_from_trending():
    """Generate video ideas based on trending topics."""
    topics = fetch_trending_topics()
    ideas = [f"How to get started with {topic}" for topic in topics]
    return ideas

if __name__ == "__main__":
    print(generate_ideas_from_trending())
