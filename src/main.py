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
    user_profiles = {
        "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.90,
        "valence": 0.90,
        "tempo_bpm": 130,
        "danceability": 0.90,
        "acousticness": 0.10
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40,
            "valence": 0.60,
            "tempo_bpm": 80,
            "danceability": 0.60,
            "acousticness": 0.75
        },

        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "valence": 0.35,
            "tempo_bpm": 155,
            "danceability": 0.65,
            "acousticness": 0.10
        },

        "Conflicting Preferences": {
            "genre": "lofi",
            "mood": "intense",
            "energy": 0.95,
            "valence": 0.10,
            "tempo_bpm": 150,
            "danceability": 0.10,
            "acousticness": 0.95
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  TOP 5 RECOMMENDATIONS: {profile_name}")
        print("=" * 50)

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec

            print(f"\n{i}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f}/9.00")
            print(f"   Reasons: {explanation}")

        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
