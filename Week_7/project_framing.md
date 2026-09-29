# Week 7 Demo 2 - Project Framing

## Project Name

Sleep Tracker

---

## Purpose

The purpose of this project is to track how much sleep I'm getting throughout the week and give appropriate feedback based on hours slept through a preset messaging system. 

---

## User

The intended user is myself of course, but this program should be usable by anyone who sleeps and wants to track it!

---

## Inputs

Inputs:
- (Estimated) Time of Slumber
- (Estimated) Time of Waking
- Day of Week

---

## Outputs

- Time Slept (Time of Waking - Time of Slumber)
- Classes on Given Day (Predetermined; listed info)
- Message about sleep quality based on Time Slept

---

## Constraints

- Will be a little weird to calculate hours based on clock input; will have to think about that when writing calculation. Maybe there is a specific way to do it in Python?

---

## Likely Structure

- Not going to do a Django or anything with HTML
- Will likely be a fully function-based program, not getting into class.
    - One function for time inputs
    - One function for calculating time inputs
    - One function for printing output hours slept + message
    - Maybe fourth function to give day of the week class info, could be built into previous function though



---

## Risks or Unknowns

- With multiple functions planned out the way they are above, I might run the risk of violating the DRY principle. In order to mitigate that, I am trying to think ahead in terms of what functions could be put together.

---

## AI-Use Boundaries

AI may help:

- suggest alternate function names
- draft a first version of a summary function
- compare organizational options

AI may not decide:

- the project purpose
- whether the project is too large
- what counts as a successful final build