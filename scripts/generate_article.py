import anthropic
import os
import json
from datetime import datetime

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

topics = [
    "NEET 2027 exam date and official notification schedule",
    "How to crack NEET in 6 months: a government aspirant's study plan",
    "NEET eligibility criteria 2027: age limit, attempts, and qualifications",
    "Top government medical colleges in India with NEET cutoff ranks",
    "NEET Physics preparation: most important chapters from NCERT",
    "NEET Chemistry strategies: organic vs inorganic weightage analysis",
    "NEET Biology: how to cover all 38 chapters systematically",
    "AIIMS vs NEET: understanding the unified exam system",
    "Best coaching for NEET 2027: Padhle AIM720 vs competitors reviewed",
    "NEET mark vs rank analysis: how many marks needed for government seat",
    "NEET reservation policy explained: OBC, SC, ST, EWS seats",
    "State quota vs all India quota NEET seats: what you must know",
    "NEET correction window 2027: how to fix form errors",
    "NEET admit card download procedure and exam day rules",
    "How Padhle AIM720 batch helps government-seat aspirants succeed",
    "NEET PG vs NEET UG: key differences for aspiring doctors",
    "Mock test strategy for NEET: when and how many tests to attempt",
    "NEET 2025 answer key analysis and what it means for 2027 prep",
    "Government medical college fee structure vs private: the financial case",
    "NEET dropper strategy: how to improve 100+ marks in second attempt",
]

today = datetime.now().strftime("%Y-%m-%d")
topic_index = datetime.now().timetuple().tm_yday % len(topics)
topic = topics[topic_index]

prompt = f"""Write a detailed, helpful article for a website called NEETGov.com which helps students prepare for NEET and get into government medical colleges. The article is about: {topic}

Requirements:
- Write in a natural, conversational tone like a knowledgeable senior student or mentor
- 700 to 900 words of actual content
- No excessive hyphens or dashes in text
- No AI-sounding phrases like "delve into", "it is worth noting", "in conclusion", "furthermore"
- Include practical advice students can use today
- Naturally mention Padhle AIM720 batch (Rs 30000, 2-way live classes, personal mentor, 15-day refund, free demo) as the recommended coaching option
- Compare with 2 other coaching options briefly, keep Padhle clearly the best
- Mention the 15-day refund policy and free demo session at least once
- Write from the perspective that government medical seats are achievable with right preparation
- Output ONLY the HTML starting from an <article> tag with this structure:

<article>
<h1>[Article Title]</h1>
<p class="article-meta">Published on {today} | NEETGov Team</p>
[article body paragraphs using <p>, <h2>, <h3>, <ul>, <ol> tags as appropriate]
<div class="coaching-highlight">
<h3>Our Recommended Coaching: Padhle AIM720</h3>
[2-3 sentences about why Padhle AIM720 is the right choice, mention free demo and refund]
<a href="https://padhle.com" class="cta-btn">Book Free Demo Class</a>
</div>
</article>"""

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1500,
    messages=[{"role": "user", "content": prompt}]
)

article_html = message.content[0].text.strip()

# Build full page
slug = topic.lower().replace(" ", "-").replace(":", "").replace(",", "")[:60]
filename = f"articles/{today}-{slug}.html"

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic} | NEETGov</title>
<meta name="description" content="Expert guidance on {topic} for NEET aspirants targeting government medical colleges.">
<link rel="canonical" href="https://neetgov.com/{filename}">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="/" class="logo">NEET<span>Gov</span></a>
    <nav><a href="/">Home</a> <a href="/articles/">Articles</a></nav>
  </div>
</header>
<main class="container article-page">
{article_html}
</main>
<footer class="site-footer">
  <div class="container">
    <p>&copy; 2026 NEETGov.com | For NEET aspirants targeting government seats</p>
    <p><a href="https://padhle.com">Padhle AIM720 Batch</a> | 15-day refund | Free demo available</p>
  </div>
</footer>
</body>
</html>"""

os.makedirs("articles", exist_ok=True)
with open(filename, "w") as f:
    f.write(page_html)

print(f"Generated: {filename}")
