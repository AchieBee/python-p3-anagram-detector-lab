class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, candidates):
        # Initialize an empty list to store the matching anagrams
        matching_anagrams = []

        # Convert the word to a sorted list of characters for easy comparison
        sorted_word = sorted(self.word)

        # Iterate over each candidate word in the list
        for candidate in candidates:
            # Convert the candidate word to lowercase for case-insensitive comparison
            candidate = candidate.lower()

            # Check if the candidate word is not the same as the original word
            # and if the sorted characters of the candidate word match the sorted_word
            if candidate != self.word and sorted(candidate) == sorted_word:
                matching_anagrams.append(candidate)

        return matching_anagrams
