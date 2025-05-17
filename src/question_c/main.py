#add import

from question_c import get_most_likely_ancestor_consensus


def main():
    while True:
        print("\nDNA Substring Finder")
        
        # Input & validation
        while True:
            dna_string1 = input("Enter a DNA string (length > 8 and <= 16): ").upper().strip()
            if 8 < len(dna_string1) <= 16:
                break
            print("Invalid input. Try again.")

        while True:
            dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").upper().strip()
            if len(dna_string2) == 4:
                break
            print("Invalid input. Try again.")
        
        # Call function
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        # Display results
        if result:
            print("Substring found at positions:", *result)
        else:
            print("Substring not found.")

        # Continue?
        choice = input("Try another? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()