# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

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

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
