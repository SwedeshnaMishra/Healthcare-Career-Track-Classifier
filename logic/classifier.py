from logic.rules import calculate_scores

def classify(candidate):
    scores = calculate_scores(candidate)

    sorted_tracks = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_3 = [track[0] for track in sorted_tracks[:3]]

    total = sum(scores.values())

    if total == 0:
        best_track = "Undetermined"
    else:
        best_track = top_3[0]

    degree_map = {
        "T01_Healthcare_Admin": "MHA",
        "T02_Consulting": "MBA-HC",
        "T03_Finance": "MBA-HC",
        "T04_Behavioral_Health": "MPH",
        "T05_Public_Health": "MPH",
        "T06_Epidemiology": "MPH",
        "T07_Policy": "MPH",
        "T08_Environmental": "MPH",
        "T09_Digital_Health": "MSHI",
        "T10_Life_Sciences": "MBA-HC",
        "T11_Entrepreneurship": "MBA-HC",
        "Undetermined": "Explore options"
    }

    top_reason = top_3[0]

    if best_track == "Undetermined":
        rationale = "Insufficient data to determine a clear career path."
    else:
        rationale = f"{candidate['name']}'s background and stated interests strongly align with {top_reason}, making it the most suitable career direction."

    result = {
        "name": candidate["name"],
        "top_3_tracks": top_3,
        "recommended_degree": degree_map.get(best_track, "MPH"),
        "rationale": rationale,
        "scores": scores
    }

    return result