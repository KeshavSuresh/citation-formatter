# Citation Formatter

A command-line tool that formats messy citation data into proper APA format.
Built as a practical tool for research assistant work in university labs.

## What it does
- Reads a plain text file containing raw citation data
- Formats each citation into proper APA style
- Handles invalid lines gracefully by skipping them
- Exports all formatted citations to a new text file
- Re-prompts if an invalid filename is entered

## Input format
Each line in your input file should follow this format:

author name, title, year, journal

Example:
smith j, silicon transistor scaling, 2021, Nature

## Output format
Smith, J. (2021). Silicon Transistor Scaling. Nature.

## How to run it
Make sure you have Python installed, then run:

    python formatter.py

You will be prompted to enter:
1. Your input filename (re-prompted if file is not found)
2. A name for the output file

## Error handling
- If the input file does not exist, the program asks again instead of crashing
- If a line does not have exactly 4 parts, it is skipped and counted
- If an author has no initials, that line is skipped

## Skills used
- Python
- File handling
- String manipulation and formatting
- Error handling with loops and conditionals

## Built by
Keshav Suresh
Incoming Waterloo Nanotechnology Engineering, Fall 2026
LinkedIn: linkedin.com/in/keshav-suresh-74926b361
