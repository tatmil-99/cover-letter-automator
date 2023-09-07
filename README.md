# cover-letter-automator

## Purpose and Summary

This is the first project I've built out of need and with intent to use on a regular basis. This was really educational and enabled me to see how code can be used in my life to automate tasks. This project is far from done, but the gist of it is this: The programs interface is the command-line, which prompts for job specific information. That data, along with the current date, is passed to a function which handles a .txt file (the cover letter). That file is then parsed and relevent information is updated and then output to a PDF in my Downloads folder. Below, I will get more into detail as far as tools and other things go.

## Tools

- Python
- Git
- datetime module
- fpdf module
- SQLite (to come)

## Features

- CRUD functionality and data persistance for past job entries (to come)
- File reading and writing
- PDF formatting and generation from .txt file
- A CLI for program interaction

## Software Development Process

- I started by figuring out what problem I wanted to solve. From here I did some analysis and asked a lot of "how" questions.
- I then began to design my algorithm for solving this problem (it was an ongoing process).
- After that I started implementing small parts of the design.
- Then I would test and do lots of debugging.
- Now a simple version is operational.
- From here I will continue to refine and add features, opening "feature" git branches when I do.

## Available Scripts

With fpdf and python3 installed, one could run `python3 letter_automator.py` inside the project directory.
