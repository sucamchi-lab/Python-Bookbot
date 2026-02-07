from stats import word_count
import sys

IGNORED_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "else", "when",
    "at", "from", "by", "for", "with", "about", "against", "between",
    "into", "through", "during", "before", "after", "above", "below",
    "to", "of", "in", "on", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "i", "me",
    "my", "we", "our", "you", "your", "he", "him", "his", "she",
    "her", "it", "its", "they", "them", "their", "which", "that", "this", "as", "all", "not",
    "some", "any", "no", "up", "down", "out", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "so"
}


def get_book_text(book):
    with open(book, "r") as f:
        return f.read()


def get_top_words(text, limit=100):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned = word.strip('.,?_!"()[]:;*#')
        if cleaned and cleaned not in IGNORED_WORDS:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:limit]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")

    print("--------- Top 100 Words ---------")
    top_words = get_top_words(book_text)
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i}. {word}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
