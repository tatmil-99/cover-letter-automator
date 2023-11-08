# Cover letter automator

## Purpose and summary

This is the first project I've built out of need and with intent to use. This was really educational and enabled me to see how code can be used in my life to automate tasks. Building my own CLI also allowed me to learn a lot about commands and the CLI in general. Upon execution of the program, an interactive CLI opens with some helpful tips and prompts for job specific information. That data, along with the current date, is passed to a function which handles a .txt file (the cover letter). That file is then parsed and relevent information is updated and then output to a PDF in my Downloads. Below, I will get more into detail as far as tools and other things go.

## Tools

- Python
- Git
- datetime module
- fpdf module
- argparse module
- SQLite (to come)

## Features

- CRUD functionality of job data using commands in the CLI
- Long term data persistance for past job entries (feature to come with SQLite) 
- File reading and writing for updating cover letter template
- PDF formatting and generation of cover letter .txt file
- Option to generate PDF cover letter without storing job data
- A CLI for program interaction
- Easy to use UI with help options for general program use and subcommands

### Example 1:

![A1291A09-33CC-4EF2-96A0-1C99B7A0C9D4](https://github.com/tatmil-99/cover-letter-automator/assets/68832615/a8f9e5f9-9e52-4138-aec5-7a41a2cfca07)

### Example 2:

![87F3E375-7E11-46AD-809C-485726AC4D83](https://github.com/tatmil-99/cover-letter-automator/assets/68832615/6570725d-2a44-4ad3-99bc-817ee6b6cd10)

## Software development process

- I started by figuring out what problem I wanted to solve. From here I did some analysis and asked a lot of "how" questions.
- I then began to design my algorithm for solving this problem (it was an ongoing process).
- After that I started implementing small parts of the design.
- Then I would test and do lots of debugging.
- Now a simple version is operational.
- From here I will continue to refine and add features, opening "feature" git branches when I do.
