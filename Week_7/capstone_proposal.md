# Week 7 Demo 5 - Capstone Proposal Example

## Project Name

Sleep Tracker

---

## Project Purpose

Design an interactive app that tracks a user's class schedule, takes inputs of bedtimes and waking times to calculate how long they slept, and tells them if they got enough sleep or not for their classes!

---

## Main Features

* Prompt user to input time going to sleep and time waking up
* Calculate the difference between two times and present in hours & minutes format
* Give the user a message regarding how much sleep they got 

---

### Potential/Backlog Features

* Have users input their own course load
    - May be difficult to add if I'm struggling with times already, but if that part is easier than I expect, it could carryover to this feature

---

## Inputs

* Time going to bed
* Time waking up
* (Potentially) Student's course load

---

## Outputs

* Time slept
* Classes for current day
* Sleep quality message

---

## Likely Structure

* List of courses, including days and times
* Function to prompt user input for time of sleeping/waking
* Function to calculate time difference (could be in above or below function? might have to make separate)
* Function to give sleep quality message to user

---

## Risks

* Making the calculation from times like 12:00 to 8:30 equal out to 8 hours and 30 minutes might be a little challenging.
    - Maybe try to convert the input times into a different numerical format before calculating?
    - Definitely check to see if Python integrates 12-hr (or 24-hr) clock formats into calculations somehow (maybe ask AI)
* Sleep quality message might not be universally accepted. Some people can get by off just 6 hrs of sleep, others need their full 8.

---

## AI Use Plan

AI may be used to:

* compare function organization
* suggest validation checks
* review output wording
(the above suggestions are all from the example template, but I like them) 
AND
* Check to see if Python can perform 12-hr clock time calculations, or assist with them if not
* Try and consolidate functions

AI will not choose:

* project purpose
* final scope
* whether the code is correct without testing
(the above suggestions are all from the example template, but I like them) 
AND
* Input values
* Courses on list

---

## Why the Scope Is Realistic

This project is not overly complex or out of scope from everything we've worked on up to this point. I don't even plan on using a class. The biggest leap here for me is probably the 12-hour format, but I have plans on how to go about working around that. Other than that, the potential for users to input their own courses might cause a hiccup, but I feel that shouldn't be overly complicated if I decide to execute on that idea.