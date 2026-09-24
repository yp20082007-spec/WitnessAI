import re


def build_timeline(text):
    """
    Create a basic chronological timeline from the
    user's incident description.

    This is the first version of the timeline engine.
    A more advanced AI-based timeline model will be
    integrated later.
    """

    events = []

    # Split the description into sentences.
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    time_pattern = r"\b(?:[01]?\d|2[0-3])(?::[0-5]\d)?\s?(?:AM|PM|am|pm)\b"

    for sentence in sentences:

        if not sentence.strip():
            continue

        time_match = re.search(
            time_pattern,
            sentence
        )

        if time_match:

            event_time = time_match.group()

            events.append({
                "time": event_time,
                "description": sentence.strip()
            })

        else:

            events.append({
                "time": "Time not specified",
                "description": sentence.strip()
            })

    return events
