## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user

So that I can manage my time

I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def estimate_reading_time(text):
    """Estimates the reading time in minutes for a given text based on 200 wpm.

    Parameters:
        text: a string containing the text to be read (e.g. "one two three ...")

    Returns:
        a float or int representing estimated reading time in minutes (e.g. 1.0 or 2)

    Side effects:
        This function has no side effects (does not print or modify global state)
    """
    pass # Test-driving means _not_ writing any code here yet.

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Given an empty string
It returns 0 (0 minutes)
"""
estimate_reading_time("") => 0

"""
Given a text with exactly 200 words
It returns 1.0 (1 minute)
"""
estimate_reading_time("...200 words...") => 1.0

"""
Given a text with 400 words
It returns 2.0 (2 minutes)
"""
estimate_reading_time("...400 words...") => 2.0

"""
Given a text with 300 words
It returns 1.5 (1.5 minutes)
"""
estimate_reading_time("...300 words...") => 1.5

"""
Given a non-string / None value
It raises an Exception
"""
estimate_reading_time(None) throws an error
```

Ensure all test function names are unique, otherwise pytest will ignore them!