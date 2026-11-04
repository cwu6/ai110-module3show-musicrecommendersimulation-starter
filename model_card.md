# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Name: MoodTunes 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is designed to suggest songs based on a user's preferred genre, mood, energy, tempo, valence, danceability, and acousticness. It creates a ranked list of the top five songs that best matches the user's preferences and provides explanations for each recommendation. Assumptions the system makes is that users can describe their music preferences through these features and that their preferences remain consistent while these recommendations are generated. This project is more intended for classroom exploration rather than real-world use because it has limited features, but it still demonstrates how recommendation algorithms use data and scoring rules to create personalized results.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The music recommender uses content based filtering, so it compares the features of each song with a user's preference to calculate how well each song matches. The recommender uses seven features: genre, mood, energy, valence (how positive or negative a soung sounds), tempo (beats per minute), danceability, and acousticness. The user profile has the preferred genre, mood, energy level, valence, tempo, danceability, and acousticness. These preferences are compared with the corresponding features of every song. The system assigns points for exact matching of genres and moods. So if it is the exact genre the user prefers, the song earns 2 points, and exact mood matches earn 1.5 points. Then for the numericl features, it calculates the similarity scores. The more closely a song's features matches the user's preferences, the higher it scores. The maximum possible score is 9 points: Genre: 2 points, Mood: 1.5 points, Energy: 1.5 points, Valence: 1 point, Tempo: 1 point, Danceability: 1 point, and Acousticness: 1 point. The program scores every song, sorts them from highest to lowest score, and returns the top five recommendations with explanations of why each song received its score. In terms of changes I made from the starter logic, I implemented the CSV, weighted scoring, and recommendation rankings. The recoommendation function evalutes every song, calculates the scores, sorts the results, and provides explanations for each song recommendation.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset

The catalog has 18 songs stored in songs.csv. Each song includes information about its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. A variety of genres are represented, including pop, lofi, rock, ambient, jazz, country, R&B, metal, reggae, classical, folk, and disco. It also includes moods such as happy, chill, intense, focused, relaxed, nostalgic, romantic, mysterious, playful, and peaceful. I added data to the original starter by including 18 songs and adding more variety in genres and moods. However, the range of the data is still small, and many genres and moods are represented by only one or two songs. It also does not include information about favorite artists or listening history.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

My system seems to works well for users who have a clear idea of the genre, mood, and features they prefer. For example, the high energy pop profile ranked sunrise city first because it matched the user's preferred pop genre, happy mood, and high energy preferences. Similarly, the chill lofi profile ranked midnight coding first because it matched the preferred lofi genre and chill mood. The deep intense rock profile also ranked storm runner first, which matched its rock and intense preferences. Another strength is that the system considers more than just genre and mood. For example, Gym Hero appeared in both the high energy pop and deep intense rock top-five recommendations because its high energy and danceability matched both profiles. This shows that numerical song features can influence recommendations even when users have different genre preferences. Overall, the results generally matched my expectations for the most part because changing a user's preferences changed the rankings. The explanations also made it easier to understand why a particular song received a high score.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender has limitations because the data only has 18 songs, with some genres represented by only one song. This may disadvantage users who prefer genres who prefer less/not represented genres or moods because they have fewer matching songs to choose from. The scoring system also requires exact genre and mood matches to receive those points, so songs with similar but not identical characteristics are not rewarded with points. For instance, songs with subgenres and mixed genres exists. Since there are fixed points awarded for genre and mood, they at top priority. It also does not consider other features such as favorite artists, listening history, or likes. Additionally, the fixed feature weights and energy similarity scoring formula may not reflect every user's preferences equally. So, users with a more unique preference may recieve recommendations that may not match what they are really looking for.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

- I tested four different user profiles to see whether the recommender changes its suggestions based on each user's music preferences:
    - High Energy Pop: User prefers pop, happy moods, high energy, upbeat songs, and high danceability
    - Chill lofi: User prefers lofi, chill moods, lower energy, slower tempos, and higher acousticness
    - Deep intense rock: User prefers refers rock, intense moods, high energy, and faster tempos
    -Conflicting preferences: User prefers lofi and acoustic songs but also wants intense moods, high energy, low valence, and faster tempos.
- I looked at whether the top recommendations matched each profile's preferences, whether different profiles received different rankings, and whether any songs appeared unexpectedly.
- Simple tests or comparisons I ran:
    - High energy pop vs chill lofi: The High-Energy Pop profile ranked Sunrise City first, while Chill Lofi ranked Midnight Coding first. This makes sense because Sunrise City has high energy and a happy pop sound, while Midnight Coding has lower energy and matches the lofi and chill preferences.
    - High energy pop vs deep intense rock High-Energy Pop ranked Sunrise City first, while Deep Intense Rock ranked Storm Runner first. Both of them preferred high energy, but their genre and mood preferences are different. Gym Hero appeared in both top five lists because it has high energy, even though its genre is pop rather than rock.
    - High energy pop vs conflicting preferences:  High energy pop ranked Sunrise City first, while Conflicting Preferences ranked Focus Flow first. This shows how genre, mood, and numerical preferences can produce different recommendations. Focus Flow matched the conflicting profile's lofi preference and multiple of its numerical features.
    - Chill lofi vs deep intense rock: Chill Lofi ranked Midnight Coding first, while Deep Intense Rock ranked Storm Runner first. Their preferences are almost opposites: Chill Lofi favors slower, calmer music, while Deep Intense Rock favors faster, more energetic music. This explains why their top recommendations are different.
    - Chill lofi vs conflicting preferences: Both ranked Focus Flow and other lofi songs highly, but their first place recommendations were different. Chill Lofi ranked Midnight Coding first, while Conflicting Preferences ranked Focus Flow first. This makes sense because the conflicting profile prefers intense moods and high energy even though it also preferred lofi.
    - Deep intense rock vs conflicting preferences: Deep Intense Rock ranked Storm Runner first, while Conflicting Preferences ranked Focus Flow first. Storm Runner matches the rock profile's genre, mood, and high  nergy preferences. Focus Flow scores highly for the conflicting profile because it matches lofi and multiple of its numerical preferences.
- Surprises: One surprise was that Gym Hero appeared in multiple recommendations, even though it is a pop song. The song's high energy and danceability allowed it to score high for users who do not specifically prefer pop. Another surprise was that Focus Flow ranked first for the conflicting preferences profile even though it has an unusual combination of preferences.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes

To improve the model next, I would make the song catalog bigger to include more genres, moods, artists, and musical styles so that users have a wider variety of recommendations. I would also add more features, such as favorite artists, likes, and listening history, to better understand individual music preferences. Another improvement would be to make the recommendation explanations more detailed by explaining how genre, mood, and numerical features contributed to each song's final score. I would also improve diversity among the top five recommendations so that users do not receive too many similar songs or songs from the same genre. Furthermore, I would also make the scoring system more flexible by allowing users to choose which features matter more. This would help my recommender handle more complex tastes instead of relying on the same fixed feature weights for everyone.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment during this project is how much changing the weights of individual features can affect recommendation rankings. When I temporarily removed the mood bonus from my scoring, the top recommendations changed for some user profiles. This helped me understand how a simple scoring system can produce personalized recommendations based on the preferences. Using AI tools helped me understand the scoring logic, identify potential biases, troubleshoot code, and compare the results from different user profiles. However, I still needed to double check the suggestions by running my program, testing it, reviewing the scoring calculations, and making sure the explanations matched the actual output. You can't automatically trust what the AI says. I was surprised that a simple algorithm using genre, mood, and numerical song features could make recommendations feel personalized. As I mentioned several times with the gym hero scenario, it showed me that algorithms can use patterns in preferences to produce recommendations. This project also changed how I think about music recommendation apps because I now understand that their suggestions depend on the data they collect and the scoring methods they use. If I extended this project, I would add a larger data of songs, allow users to customize how much each feature matters, and use listening history to make recommendations even more personalized and diverse.
