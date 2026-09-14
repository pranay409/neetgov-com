import anthropic
import os
import json
import random
from datetime import datetime

AUTHORS = ["Ananya Sharma", "Rohan Verma", "Priya Nair", "Arjun Mehta", "Sneha Iyer", "Karan Malhotra", "Divya Reddy", "Aditya Joshi"]

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
author = random.choice(AUTHORS)

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
[article body paragraphs using <p>, <h2>, <h3>, <ul>, <ol> tags as appropriate]
<div class="coaching-highlight">
<h3>Our Recommended Coaching: Padhle AIM720</h3>
[2-3 sentences about why Padhle AIM720 is the right choice, mention free demo and refund]
<a href="https://neet.padhle.in" class="cta-btn">Book Free Demo Class</a>
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
<style>
  body {{ margin: 0; font-family: -apple-system, "Segoe UI", Arial, sans-serif; color: #1a2233; background: #fff; line-height: 1.7; }}
  .container {{ max-width: 760px; margin: 0 auto; padding: 0 20px; }}
  .site-header {{ background: #0C1B33; padding: 18px 0; }}
  .site-header .container {{ display: flex; justify-content: space-between; align-items: center; }}
  .site-header .logo {{ color: #fff; font-weight: 700; font-size: 1.2rem; text-decoration: none; }}
  .site-header .logo span {{ color: #E8A020; }}
  .site-header nav a {{ color: rgba(255,255,255,0.8); text-decoration: none; margin-left: 18px; font-size: 0.92rem; }}
  .article-page {{ padding: 40px 20px 56px; }}
  .article-page h1 {{ color: #0C1B33; font-size: 1.8rem; margin-bottom: 6px; }}
  .article-meta {{ color: #6b7280; font-size: 0.85rem; margin-bottom: 24px; }}
  .article-page h2 {{ color: #0C1B33; font-size: 1.3rem; margin-top: 32px; }}
  .article-page h3 {{ color: #1A2F52; font-size: 1.05rem; }}
  .article-page p, .article-page li {{ color: #333d4f; font-size: 1.02rem; }}
  .coaching-highlight {{ background: #FFF6E0; border-left: 4px solid #E8A020; padding: 20px 24px; border-radius: 0 10px 10px 0; margin: 32px 0; }}
  .coaching-highlight h3 {{ margin-top: 0; color: #0C1B33; }}
  .cta-btn {{ display: inline-block; background: #E8A020; color: #0C1B33; padding: 10px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; margin-top: 10px; }}
  .site-footer {{ background: #0C1B33; color: rgba(255,255,255,0.75); padding: 24px 0; margin-top: 40px; font-size: 0.88rem; }}
  .site-footer a {{ color: #E8A020; }}
</style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="/" class="logo">NEET<span>Gov</span></a>
    <nav><a href="/">Home</a> <a href="/articles/">Articles</a></nav>
  </div>
</header>
<main class="container article-page">
<p class="article-meta">By <a href="https://neet.padhle.in" style="color:#E8A020;text-decoration:none;font-weight:600;">{author}</a> &middot; Published on {today}</p>
{article_html}
</main>
<footer class="site-footer">
  <div class="container">
    <p>&copy; 2026 NEETGov.com | For NEET aspirants targeting government seats</p>
    <p><a href="https://neet.padhle.in">Padhle AIM720 Batch</a> | 15-day refund | Free demo available</p>
  </div>
</footer>
</body>
</html>"""

os.makedirs("articles", exist_ok=True)
with open(filename, "w") as f:
    f.write(page_html)

print(f"Generated: {filename}")
