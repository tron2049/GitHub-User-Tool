from cli import user_activity
from api import fetch_user_activity
from parser import parse_activity

def main():  #Executes the CLI tool
    
    args = user_activity()
    if args.command == 'username':
        username = args.name
    
    events = fetch_user_activity(username)
    if events is None:
        print("Could not fetch user activity")
        return

    formatted_events = parse_activity(events)

    if not formatted_events:
        print(f"No events found for user {username}")
        
    else:
        print(f"Recent activity for {username}")
        for line in formatted_events:
            print(line)


if __name__ == "__main__":
    main()