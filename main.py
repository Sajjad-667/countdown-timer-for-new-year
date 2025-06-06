import time

def countdown_timer(seconds):
    """Countdown timer that prints time remaining every second."""
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("Time's up!")  # Message after countdown ends

# Example usage
seconds = int(input("Enter countdown time in seconds: "))
countdown_timer(seconds)
