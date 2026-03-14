import os

# -----------------------------------------------
# Citation Formatter
# Built by Keshav Suresh
# Formats messy citations into proper APA format
# -----------------------------------------------

print("Citation Formatter")
print("------------------")

# Keep asking until a valid file is entered
input_file = input("Enter your citations filename: ")

while not os.path.exists(input_file):
    print("Error: File '" + input_file + "' not found. Try again.")
    input_file = input("Enter your citations filename: ")

output_file = input("Enter output filename (e.g. formatted.txt): ")

file = open(input_file, "r")
outfile = open(output_file, "w")

count = 0
errors = 0

for line in file:
    parts = line.strip().split(",")

    # Check if line has exactly 4 parts
    if len(parts) != 4:
        print("Skipping invalid line: " + line.strip())
        errors += 1
        continue

    author = parts[0].strip().title()
    title = parts[1].strip().title()
    year = parts[2].strip()
    journal = parts[3].strip()

    author_parts = author.split()

    # Check if author has both first and last name
    if len(author_parts) < 2:
        print("Skipping invalid author: " + author)
        errors += 1
        continue

    last_name = author_parts[0]
    initials = author_parts[1] + "."
    formatted_author = last_name + ", " + initials

    citation = formatted_author + " (" + year + "). " + title + ". " + journal + "."
    outfile.write(citation + "\n")
    count += 1

file.close()
outfile.close()

# Summary
print("----------------------")
print("Citations formatted: " + str(count))
if errors > 0:
    print("Lines skipped: " + str(errors))
print("Saved to: " + output_file)
print("Done.")