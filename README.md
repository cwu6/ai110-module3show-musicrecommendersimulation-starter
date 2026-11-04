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


Real world recommendations and what version I will prioritize:
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

Algorithm Recipe/My plan:
- Content-based filtering to recommend songs based on a user's music preference. The system compares the features of each song with the user's preferred features. 
- Each song includes the following features:
Genre, Mood, Energy, Tempo (BPM), Valence, Danceability, Acousticness
- Example User Profile:
Feature:          User Preference:
Genre              lofi
Mood               chill
Energy             0.40
Valence            0.60
Tempo              80 BPM
Danceability       0.60
Acousticness       0.75
For the system, preferences could be entered directly by the user or estimnated based on the songs they like.
- Overall Scoring: Each song is scored based on how closely the featurs matches the user's preferences. The system uses seven features each with a different weight, to score a maximum of 9 points. Genre recieves the highest weight since a user's preferred music style is important. Also, mood recieves the second highest weight since it helps identify the type of listening experience the user wants.
Feature:        Max Points:     Scoring:
Genre           2.0             2 points for exact match, otherwise 0
Mood            1.5             1.5 points for exact match, otherwise 0
Energy          1.0             Based on how close to the target
Valence         1.0             Based on how close to the target
Tempo           1.0             Based on how close to the target BPM
Danceability    1.0             Based on how close to the target
Acousticness    1.0             Based on how close to the target
Total:          9.0
- Numerical Scoring: For the features that need the system to award points based on how close a song's value matches the user's target
Similarity = max(0, 1 - abs(song_value - target_value) / range)
The similarity value is multiplied by the feature's maximum points:
Feature Points = Similarity × Maximum Points
For energy, valence, danceability, and acousticness, the comparison range is 1 because these features use a 0–1 scale.
For tempo, the comparison range is 200 BPM because tempo is measured in beats per minute rather than on a 0–1 scale.
- Example Numerical Scoring: User's target energy: 0.40 Song's energy: 0.42
Similarity = 1 - abs(0.42 - 0.40) / 1
Similarity = 0.98
Since energy is worth 1.5 points: Energy Points = 0.98 × 1.5 = 1.47
The song earns 1.47 out of 1.5 possible energy points.
Final Score: The total score is calculated by adding the points from all seven features: Total Score = Genre + Mood + Energy + Valence + Tempo + Danceability + Acousticness. The maximum possible score is 9 points. Songs with higher scores are gonna be recommended since they are better matches for the user's preferences.
- Ranking and Recommendations:
The recommender evaluates every song in songs.csv individually using the same scoring rules.
After scoring all songs, the system: Stores each song with its total score, sorts songs from highest score to lowest score, selects the top five songs (K = 5), and displays the recommended songs with their scores and explanations.
- Potential Biases:
There are several potential biases:
Genre bias: Since genre recieves the highest weight, the system might prioritize songs from a preferred genre even when songs from other genres may match the user's mood and numerical preferences more closely.
Mood bias: Mood is surbjective, so when people may describe the same song as different a different mood and vibe.
Limited Personlization: The system uses a small datatset of 18 songs, so the recommendation doesn't represent a wide range of music. Also, a fixed user profile means that it ignores other things like history, skips, and likes of songs. Furthermore, there are seven feature sbeing evaluated, so the features are limited and doesn't take into account things like artist preferences or subgenres.



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
==================================================
          TOP 5 SONG RECOMMENDATIONS
==================================================

1. Sunrise City - Neon Echo
   Score: 8.92/9.00
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.47), valence similarity (+0.99), tempo similarity (+0.99), danceability similarity (+0.99), acousticness similarity (+0.98)

2. Gym Hero - Max Pulse
   Score: 6.93/9.00
   Reasons: genre match (+2.0), energy similarity (+1.30), valence similarity (+0.92), tempo similarity (+0.94), danceability similarity (+0.92), acousticness similarity (+0.85)

3. Rooftop Lights - Indigo Parade
   Score: 6.71/9.00
   Reasons: mood match (+1.5), energy similarity (+1.44), valence similarity (+0.96), tempo similarity (+0.98), danceability similarity (+0.98), acousticness similarity (+0.85)

4. Golden Horizon - Sol Mariposa
   Score: 6.70/9.00
   Reasons: mood match (+1.5), energy similarity (+1.43), valence similarity (+0.94), tempo similarity (+0.97), danceability similarity (+0.90), acousticness similarity (+0.96)

5. Afterglow Avenue - Noah Blue
   Score: 5.26/9.00
   Reasons: energy similarity (+1.48), valence similarity (+0.98), tempo similarity (+0.99), danceability similarity (+0.89), acousticness similarity (+0.92)

==================================================
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



