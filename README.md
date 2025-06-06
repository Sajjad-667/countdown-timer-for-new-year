# Countdown Timer in Python

This Python script implements a simple countdown timer that takes user input in seconds and counts down to zero, displaying the time remaining in a `MM:SS` format.

## Features
- Accepts user input for the countdown duration.
- Displays time remaining in minutes and seconds (`MM:SS` format).
- Updates the timer dynamically on the same line.
- Waits 1 second between updates using `time.sleep(1)`.
- Prints "Time's up!" when the countdown reaches zero.

## How It Works
1. The script takes an integer input from the user representing the countdown time in seconds.
2. It calculates the minutes and seconds using `divmod()`.
3. The timer updates every second and prints the remaining time on the same line.
4. Once the timer reaches zero, it displays a "Time's up!" message.

## Example Code

```python
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
```
