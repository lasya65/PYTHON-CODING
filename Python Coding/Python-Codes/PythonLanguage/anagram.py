from itertools import permutations

def generate_anagrams(word):
    # Use permutations to find all possible arrangements
    anagrams = [''.join(p) for p in permutations(word)]
    # Remove duplicates (in case of repeated letters)
    return set(anagrams)

# Test the function
word = input("Enter a word: ")
anagrams = generate_anagrams(word)
print(f"Anagrams of '{word}':")
print('\n'.join(anagrams))
