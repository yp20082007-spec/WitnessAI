import re


def extract_basic_facts(text):
    """
    Extract basic factual information from the user's description.

    This is the first-stage fact extraction layer.
    The AI model will be integrated into this module later.
    """

    facts = {
        "time": [],
        "location": [],
        "people": [],
        "objects": [],
        "events": []
    }

    # -----------------------------
    # Time extraction
    # -----------------------------

    time_pattern = r"\b(?:[01]?\d|2[0-3])(?::[0-5]\d)?\s?(?:AM|PM|am|pm)\b"

    times = re.findall(time_pattern, text)

    if times:
        facts["time"] = list(dict.fromkeys(times))

    # -----------------------------
    # Location keywords
    # -----------------------------

    location_keywords = [
        "college",
        "school",
        "hospital",
        "library",
        "hostel",
        "office",
        "road",
        "street",
        "station",
        "market",
        "gate",
        "parking",
        "home"
    ]

    for word in location_keywords:
        if re.search(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE):
            facts["location"].append(word)

    # -----------------------------
    # People indicators
    # -----------------------------

    people_patterns = [
        r"\b\d+\s+(?:people|persons|students|men|women|children)\b",
        r"\b(?:man|woman|person|student|child|driver|witness)\b"
    ]

    for pattern in people_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:
            if match not in facts["people"]:
                facts["people"].append(match)

    # -----------------------------
    # Common objects
    # -----------------------------

    object_keywords = [
        "car",
        "bike",
        "motorcycle",
        "scooter",
        "phone",
        "bag",
        "laptop",
        "vehicle",
        "door",
        "window"
    ]

    for word in object_keywords:
        if re.search(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE):
            facts["objects"].append(word)

    # -----------------------------
    # Event indicators
    # -----------------------------

    event_keywords = [
        "accident",
        "hit",
        "crashed",
        "collision",
        "fell",
        "followed",
        "entered",
        "left",
        "stopped",
        "shouted",
        "argued",
        "broke",
        "damaged"
    ]

    for word in event_keywords:
        if re.search(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE):
            facts["events"].append(word)

    return facts


def find_missing_information(facts):
    """
    Identify information that was not provided.
    """

    missing = []

    if not facts["time"]:
        missing.append("Approximate time of the incident")

    if not facts["location"]:
        missing.append("Location of the incident")

    if not facts["people"]:
        missing.append("People involved or present")

    if not facts["objects"]:
        missing.append("Relevant objects or vehicles")

    if not facts["events"]:
        missing.append("Description of what happened")

    return missing
