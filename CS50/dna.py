import csv
from sys import argv


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
    
    # Opens the CSV file and reads into it
    file_CSV = open(argv[1], "r")
    data = csv.DictReader(file_CSV)
    # Opens, reads, and closes the txt file containing the DNA sequence
    with open(argv[2]) as file_DNA:
        sequence = file_DNA.read()

    # Empty dictionary declared to track
    track_dict = {}
    for str_pattern in data.fieldnames[1:]:
        track_dict[str_pattern] = match(sequence, str_pattern)

    # Checks if portion of DNA matches or does not
    for row in data:
        if all(track_dict[str_pattern] == int(row[str_pattern]) for str_pattern in track_dict):
            print(row["name"])
            file_CSV.close()
            return
    print("No match")
    file_CSV.close()

# Custom function to determine the length and occurrence of a sequence


def match(sequence, str_pattern):
    longest = 0
    length = len(str_pattern)
    for i in range(len(sequence)):
        occurrence = 0
        while True:
            start = i + length * occurrence
            end = start + length
            if sequence[start:end] == str_pattern:
                occurrence += 1
            else:
                break
        longest = max(longest, occurrence)
    return longest


main()
