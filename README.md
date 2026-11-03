# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real world music recommendation systems like Spotify use collaborative
filtering, meaning that it look at multiple aspects. For instance, it
looks at the listening behavior of similar users and use content-based
filtering, which looks at a song's characteristics and check how likely
the user would like it. My version will prioritize content-based filtering
by comparing a song's attributes and features with a user's preferences.
The Recommender will calculate a score for each song based on how closely 
the song's features matches the user's preferences. In terms of genre and mood,
it will check how closely it matches the user's choices. In terms of energy, 
valence, tempo, danceability, and acousticness, it will check how closely it 
matches the user's preferred numerical values/levels of those features (0-1 scale
for most and bpm for tempo). and acousticness, Songs with higher overall scores
will be ranked higher and the recommender will select the tops songs to recommend. 
In 'Song', features I  will include are the title, artist genre, mood (vibe of the 
song), energy  (intensity level), tempo_bpm (speed  of the song in beats per minute), 
valence (how positive the song sounds), danceability (how good the song is for dancing), 
and acousticness (how acosutic the song sounds). For 'UserProfile', it will store 
preferred_genre (the user's preferred genre), preferred_mood (user's preferred mood), 
preferred_energy (user's preferred energy level), preferred_valence (user's preferred
positivity level), and preferred_tempo_bpm (user's preferred tempo in beats per minute).
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



