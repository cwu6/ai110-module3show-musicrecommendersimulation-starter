# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

In this project, my version implements a CLI-first music recommender that suggests songs based on a user's music preferences. It uses song features such as genre, mood, energy, tempo, valence, danceability, and acousticness to calculate a score for each song. The system ranks songs by their scores and displays the top five recommendations along with explanations of why each song was recommended. I also tested different user profiles and experimented with removing the mood feature to understand how individual preferences affected the recommendations.

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
positivity level), preferred_tempo_bpm (user's preferred tempo in beats per minute), preferred_danceability (the user's preferred danceability level), and preferred_acousticness (the user's preferred acousticness level).

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
- Overall Scoring: Each song is scored based on how closely the featurs matches the user's preferences. The system uses seven features each with a different weight, to score a maximum of 9 points. Genre recieves the highest weight since a user's preferred music style is important. Also, mood recieves the second highest weight since it helps identify the type of listening experience the user wants.
Feature:        Max Points:     Scoring:
Genre           2.0             2 points for exact match, otherwise 0
Mood            1.5             1.5 points for exact match, otherwise 0
Energy          1.5             Based on how close to the target
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

Accuracy and Suprises:
I compared the chill lofi recommendations with my musical intuition. The results felt reasonable because midnight coding and library rain ranked first and second. Both songs match the preferred lofi genre and chill mood. Midnight doding ranked first with 8.86/9.00, which is slightly ahead of library rain with 8.76/9.00. Both received the full genre and mood points, but midnight coding received a higher combined score from its numerical feature similarities. One interesting observation was that focus flow ranked third even though it did not match the preferred chill mood. This showed that numerical feature similarities can still help a song rank highly even without matching every preference.

Data Experiment: Removing Mood Weight
For this experiment, I temporarily commented out the mood-matching portion of my scoring algorithm while keeping all other weights the same. This reduced the maximum possible score from 9.0 to 7.5 points. The experiment made some interesting changes:
- High energy pop: Gym hero replaced sunrise city as the top recommendation
- Chill lofi: Focus flow replaced midnight coding as the top recommendation.
- Deep intense rock: Storm runner remained the top recommendation.
- Conflicting preferences: Focus flow remained first, although the other rankings changed.
The experiment showed that mood is an important feature in my recommender. Without the 1.5 points from it, songs with stronger numerical similarities sometimes ranked higher, even if they did not match the user's preferred mood.Overall, removing mood made the recommendations different, but not it didn't really make it more accurate. For example, the original chill lofi results seemed more appropriate because midnight coding and library rain both matched the user's preferred chill mood. This experiment helped me understand how much individual feature and their weights can influence recommendation rankings.

Stress Test With Diverse Profiles:
```
==================================================
  TOP 5 RECOMMENDATIONS: High-Energy Pop
==================================================

1. Sunrise City - Neon Echo
   Score: 8.57/9.00
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.38), valence similarity (+0.94), tempo similarity (+0.94), danceability similarity (+0.89), acousticness similarity (+0.92)

2. Gym Hero - Max Pulse
   Score: 7.25/9.00
   Reasons: genre match (+2.0), energy similarity (+1.46), valence similarity (+0.87), tempo similarity (+0.99), danceability similarity (+0.98), acousticness similarity (+0.95)

3. Golden Horizon - Sol Mariposa
   Score: 6.83/9.00
   Reasons: mood match (+1.5), energy similarity (+1.42), valence similarity (+0.99), tempo similarity (+0.98), danceability similarity (+1.00), acousticness similarity (+0.94)

4. Rooftop Lights - Indigo Parade
   Score: 6.34/9.00
   Reasons: mood match (+1.5), energy similarity (+1.29), valence similarity (+0.91), tempo similarity (+0.97), danceability similarity (+0.92), acousticness similarity (+0.75)

5. Afterglow Avenue - Noah Blue
   Score: 5.20/9.00
   Reasons: energy similarity (+1.33), valence similarity (+0.93), tempo similarity (+0.96), danceability similarity (+0.99), acousticness similarity (+0.98)

==================================================

==================================================
  TOP 5 RECOMMENDATIONS: Chill Lofi
==================================================

1. Midnight Coding - LoRoom
   Score: 8.86/9.00
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.47), valence similarity (+0.96), tempo similarity (+0.99), danceability similarity (+0.98), acousticness similarity (+0.96)

2. Library Rain - Paper Lanterns
   Score: 8.76/9.00
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.42), valence similarity (+1.00), tempo similarity (+0.96), danceability similarity (+0.98), acousticness similarity (+0.89)

3. Focus Flow - LoRoom
   Score: 7.46/9.00
   Reasons: genre match (+2.0), energy similarity (+1.50), valence similarity (+0.99), tempo similarity (+1.00), danceability similarity (+1.00), acousticness similarity (+0.97)

4. Spacewalk Thoughts - Orbit Bloom
   Score: 6.31/9.00
   Reasons: mood match (+1.5), energy similarity (+1.32), valence similarity (+0.95), tempo similarity (+0.90), danceability similarity (+0.81), acousticness similarity (+0.83)

5. Autumn Letters - Willow Creek
   Score: 5.22/9.00
   Reasons: energy similarity (+1.38), valence similarity (+0.98), tempo similarity (+0.94), danceability similarity (+0.95), acousticness similarity (+0.97)

==================================================

==================================================
  TOP 5 RECOMMENDATIONS: Deep Intense Rock
==================================================

1. Storm Runner - Voltline
   Score: 8.79/9.00
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.44), valence similarity (+0.87), tempo similarity (+0.98), danceability similarity (+0.99), acousticness similarity (+1.00)

2. Gym Hero - Max Pulse
   Score: 6.16/9.00
   Reasons: mood match (+1.5), energy similarity (+1.47), valence similarity (+0.58), tempo similarity (+0.89), danceability similarity (+0.77), acousticness similarity (+0.95)

3. Shadow Temple - Iron Veil
   Score: 5.18/9.00
   Reasons: energy similarity (+1.48), valence similarity (+0.96), tempo similarity (+0.97), danceability similarity (+0.84), acousticness similarity (+0.92)

4. Night Drive Loop - Neon Echo
   Score: 4.63/9.00
   Reasons: energy similarity (+1.20), valence similarity (+0.86), tempo similarity (+0.78), danceability similarity (+0.92), acousticness similarity (+0.88)

5. Sunrise City - Neon Echo
   Score: 4.41/9.00
   Reasons: energy similarity (+1.30), valence similarity (+0.51), tempo similarity (+0.81), danceability similarity (+0.86), acousticness similarity (+0.92)

==================================================

==================================================
  TOP 5 RECOMMENDATIONS: Conflicting Preferences
==================================================

1. Focus Flow - LoRoom
   Score: 5.16/9.00
   Reasons: genre match (+2.0), energy similarity (+0.68), valence similarity (+0.51), tempo similarity (+0.65), danceability similarity (+0.50), acousticness similarity (+0.83)

2. Storm Runner - Voltline
   Score: 5.14/9.00
   Reasons: mood match (+1.5), energy similarity (+1.44), valence similarity (+0.62), tempo similarity (+0.99), danceability similarity (+0.44), acousticness similarity (+0.15)

3. Library Rain - Paper Lanterns
   Score: 5.14/9.00
   Reasons: genre match (+2.0), energy similarity (+0.60), valence similarity (+0.50), tempo similarity (+0.61), danceability similarity (+0.52), acousticness similarity (+0.91)

4. Midnight Coding - LoRoom
   Score: 5.12/9.00
   Reasons: genre match (+2.0), energy similarity (+0.70), valence similarity (+0.54), tempo similarity (+0.64), danceability similarity (+0.48), acousticness similarity (+0.76)

5. Gym Hero - Max Pulse
   Score: 4.53/9.00
   Reasons: mood match (+1.5), energy similarity (+1.47), valence similarity (+0.33), tempo similarity (+0.91), danceability similarity (+0.22), acousticness similarity (+0.10)

==================================================
```
---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This recommender has several limitations. It uses a small dataset of only 18 songs, so it cannot represent every genre, mood, or different types of music in general. It also does not analyze likes or personal listening history. Moreover, the scoring system uses fixed weights and exact genre and mood matches, which may favor certain preferences over others. As a result, some users may receive recommendations that are not to their liking, especially if their preferred genres or moods are not represented in the dataset.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

- Through this project, I learned how a recommender system turns information about songs and user preferences into numerical scores to generate recommendations. I learned that different features can have different weights, meaning some preferences influence the final rankings more than others. Doing the testing for multiple user profiles helped me understand how changing preferences affects the recommendations. For example, gym hero appeared in both the high energy pop and deep intense rock recommendations because both profiles preferred high energy music, even though they had different genre preferences. I also learned that recommender systems can have bias depending on the data and scoring rules they use. For example, a small dataset with many non represented genres can limit the recommendations available to certain users. Fixed scoring weights can also cause the system to prioritize some preferences over others. My experiment removing mood from the scoring logic showed me how changing one feature can significantly affect rankings.



