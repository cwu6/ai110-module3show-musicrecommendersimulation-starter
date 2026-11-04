from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_valence: float = 0.60
    target_tempo_bpm: float = 80
    target_danceability: float = 0.60
    target_acousticness: float = 0.75

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.5

            score += max(0, 1 - abs(song.energy - user.target_energy)) * 1.5
            score += max(0, 1 - abs(song.valence - user.target_valence))
            score += max(0, 1 - abs(song.tempo_bpm - user.target_tempo_bpm) / 200)
            score += max(0, 1 - abs(song.danceability - user.target_danceability))
            score += max(0, 1 - abs(song.acousticness - user.target_acousticness))

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [item[0] for item in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre match")

        if song.mood == user.favorite_mood:
            reasons.append("mood match")

        if abs(song.energy - user.target_energy) < 0.2:
            reasons.append("similar energy")

        if abs(song.valence - user.target_valence) < 0.2:
            reasons.append("similar valence")

        if abs(song.tempo_bpm - user.target_tempo_bpm) < 20:
            reasons.append("similar tempo")

        if abs(song.danceability - user.target_danceability) < 0.2:
            reasons.append("similar danceability")

        if abs(song.acousticness - user.target_acousticness) < 0.2:
            reasons.append("similar acousticness")

        if not reasons:
            return "No strong preference matches."

        return "Recommended because of: " + ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return them as a list of dictionaries."""
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            }

            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate how well a song matches the user's preferences."""
    total_score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        total_score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        total_score += 1.5
        reasons.append("mood match (+1.5)")

    energy_similarity = max(0, 1 - abs(song["energy"] - user_prefs["energy"]) / 1)
    energy_points = energy_similarity * 1.5
    total_score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    valence_similarity = max(0, 1 - abs(song["valence"] - user_prefs["valence"]) / 1)
    valence_points = valence_similarity * 1.0
    total_score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    tempo_similarity = max(0, 1 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 200)
    tempo_points = tempo_similarity * 1.0
    total_score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    danceability_similarity = max(0, 1 - abs(song["danceability"] - user_prefs["danceability"]) / 1)
    danceability_points = danceability_similarity * 1.0
    total_score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    acousticness_similarity = max(0, 1 - abs(song["acousticness"] - user_prefs["acousticness"]) / 1)
    acousticness_points = acousticness_similarity * 1.0
    total_score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    return total_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by preference score with explanations."""
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = ", ".join(reasons)

        recommendations.append((song, score, explanation))

    recommendations = sorted(
        recommendations,
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return recommendations[:k]
