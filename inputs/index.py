# Creative Story Generator - A Fun Python Program for Beginners

# Print a welcome message
print("=" * 50)
print("Welcome to the Creative Story Generator!")
print("=" * 50)
print()

# Collect user inputs with clear prompts
adjective = input("Enter an adjective (e.g., scary, funny, tiny): ")
verb_1 = input("Enter a verb (e.g., running, jumping, dancing): ")
animal = input("Enter an animal (e.g., cat, dragon, penguin): ")
exclamation = input("Enter an exclamation word (e.g., Help, Wow, Oh no): ")
verb_2 = input("Enter another verb (e.g., scream, laugh, hide): ")
verb_3 = input("Enter one more verb (e.g., explode, sing, vanish): ")

# Create the story by combining the user inputs with the template
story = (
    "The other day, I was really in trouble. It all started when I saw a very\n"
    f"{adjective} {animal} {verb_1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
    f"I could think to do was to {verb_2} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {verb_3}\n"
    "right in front of my family."
)

# Display the final story
print()
print("=" * 50)
print("Here's your story:")
print("=" * 50)
print()
print(story)
print()
print("=" * 50)

