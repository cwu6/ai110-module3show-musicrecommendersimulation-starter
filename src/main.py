"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "valence": 0.85,
        "tempo_bpm": 120,
        "danceability": 0.80,
        "acousticness": 0.20
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("          TOP 5 SONG RECOMMENDATIONS")
    print("=" * 50)

    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec

        print(f"\n{i}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}/9.00")
        print(f"   Reasons: {explanation}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
