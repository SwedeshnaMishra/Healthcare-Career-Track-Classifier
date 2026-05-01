def calculate_scores(candidate):
    track_score = {
        "T01_Healthcare_Admin": 0,
        "T02_Consulting": 0,
        "T03_Finance": 0,
        "T04_Behavioral_Health": 0,
        "T05_Public_Health": 0,
        "T06_Epidemiology": 0,
        "T07_Policy": 0,
        "T08_Environmental": 0,
        "T09_Digital_Health": 0,
        "T10_Life_Sciences": 0,
        "T11_Entrepreneurship": 0
    }

    subjects = [s.lower() for s in candidate.get("subjects", [])]
    sop = candidate.get("sop", "").lower()
    experience = candidate.get("experience", "").lower()

    if any(sub in subjects for sub in ["biology", "anatomy", "physiology", "pharmacology"]):
        track_score["T10_Life_Sciences"] += 3
        track_score["T05_Public_Health"] += 2

    if any(sub in subjects for sub in ["python", "database", "machine learning", "cloud"]):
        track_score["T09_Digital_Health"] += 4

    if any(sub in subjects for sub in ["finance", "accounting", "economics"]):
        track_score["T03_Finance"] += 4
        track_score["T01_Healthcare_Admin"] += 2

    if any(sub in subjects for sub in ["sociology", "psychology", "community"]):
        track_score["T05_Public_Health"] += 3
        track_score["T07_Policy"] += 2

    if "leadership" in sop or "management" in sop:
        track_score["T01_Healthcare_Admin"] += 4

    if "policy" in sop or "government" in sop:
        track_score["T07_Policy"] += 4

    if "data" in sop or "analytics" in sop:
        track_score["T06_Epidemiology"] += 3
        track_score["T09_Digital_Health"] += 2

    if "technology" in sop or "ehr" in sop:
        track_score["T09_Digital_Health"] += 4

    if "community" in sop or "health equity" in sop:
        track_score["T05_Public_Health"] += 4

    if "finance" in sop or "cfo" in sop:
        track_score["T03_Finance"] += 4

    if "nurse" in experience or "clinical" in experience:
        track_score["T01_Healthcare_Admin"] += 3

    if "developer" in experience or "software" in experience:
        track_score["T09_Digital_Health"] += 3

    if "audit" in experience or "finance" in experience:
        track_score["T03_Finance"] += 3

    if "ngo" in experience or "community" in experience:
        track_score["T05_Public_Health"] += 3

    return track_score