from datetime import datetime



def parse_activity(events, limit=10):   #Prints the user ativity formated in plain tecxt
    
    parsed_events = []

    if not events:
        return parsed_events

    if not isinstance(events, list):
        return [f"Error: {events.get('message', str(events))}"]

    for event in events[:limit]:
        event_type = event.get("type", "UnknownEvent")
        repo_name = event.get("repo", {}).get("name", "UnknownRepo")
        event_created = event.get("created_at", "")

        try:
            dt = datetime.fromisoformat(event_created.replace("Z", "+00:00"))
            date_str = dt.strftime("%d/%m/%Y, %H:%M")
        except Exception:
            date_str = event_created

        extra_info = ""
        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            messages = [commit.get("message", "") for commit in commits]
            if messages:
                extra_info = " - " + " | ".join(messages)

        formatted = f"[{date_str}] {event_type} en {repo_name}{extra_info}"
        parsed_events.append(formatted)

    return parsed_events
