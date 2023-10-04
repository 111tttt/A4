from Spinner import Spinner
import string
# Jordan Reynolds
# Assignment 4

def process_text(text):
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def main():
    # Load the essay text
    with open('essay.txt', 'r') as file:
        essay_text = file.read()

    # Process the essay text
    essay_text = process_text(essay_text)

    # Create a Spinner object with the synonym file
    spinner = Spinner('synonyms-simplified.txt')

    # Print the original text
    print("Original:", essay_text)

    # Change the text three times using the Spinner
    for i in range(3):
        spun_text = spinner.spin_text(essay_text)
        print(f"Option {i + 1}:", spun_text)


if __name__ == "__main__":
    main()
