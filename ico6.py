def read_lyrics(filename):
    with open(filename, 'r') as file:
        return file.read().lower().split()

def create_word_count(lyrics):
    word_count = {}
    for word in lyrics:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    # Prompt the user for the first artist and their lyrics file
    artist1 = input("Enter the name of the first artist: ")
    artist1_file = input("Enter the filename for {}'s lyrics: ".format(artist1))
    artist1_lyrics = read_lyrics(artist1_file)
    artist1_word_count = create_word_count(artist1_lyrics)

    # Prompt the user for the second artist and their lyrics file
    artist2 = input("Enter the name of the second artist: ")
    artist2_file = input("Enter the filename for {}'s lyrics: ".format(artist2))
    artist2_lyrics = read_lyrics(artist2_file)
    artist2_word_count = create_word_count(artist2_lyrics)

    # Ask the user for a lyric to predict
    lyric = input("Enter a lyric: ")
    lyric_words = lyric.lower().split()

    # Initialize sums for both artists
    artist1_sum = 0
    artist2_sum = 0

    # Calculate sums for each artist based on word frequencies
    for word in lyric_words:
        artist1_sum += artist1_word_count.get(word, 0)
        artist2_sum += artist2_word_count.get(word, 0)

    # Predict the artist based on the sums
    if artist1_sum > artist2_sum:
        print("Prediction: '{}' is more likely sung by {}.".format(lyric, artist1))
    elif artist1_sum < artist2_sum:
        print("Prediction: '{}' is more likely sung by {}.".format(lyric, artist2))
    else:
        print("Prediction: It's difficult to predict. Both artists may have sung '{}'.".format(lyric))

if __name__ == "__main__":
    main()