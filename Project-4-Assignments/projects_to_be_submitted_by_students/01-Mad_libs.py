def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please provide the following words:")
    
    # Get user input for various word types
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb_past = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter a plural noun: ")
    adjective3 = input("Enter one more adjective: ")
    verb = input("Enter a verb: ")
    
    # The Mad Lib story template
    story = f"""
    Once upon a time, in a {adjective1} {noun1}, there lived a brave adventurer. 
    One day, they {verb_past} {adverb} into the {adjective2} {noun2}. 
    There, they found a treasure chest full of {noun3}! 
    "This is {adjective3}!" they exclaimed, and decided to {verb} all the way home.
    
    THE END
    """
    
    # Display the completed story
    print("\nHere's your Mad Lib story:\n")
    print(story)


if __name__ == "__main__":
    mad_libs()