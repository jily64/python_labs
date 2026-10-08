from src.lib.text import normalize, tokenize, count_freq, top_n
import sys, unicodedata


if __name__ == "__main__":
    """
    Берем текст из консоли, нормализуем, закидываем в токенизатор, считаем частоту слов, выводим топ 5 слов.
    
    Чего то необычного тут нет.
    """
    
    stdin_text = sys.stdin.read()
    
    normalized_text = normalize(stdin_text)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ 5 слов:")
    
    max_word_length = max(max(len(word) for word, _ in top_words), len("слово"))
    
    # Для красаты
    max_word_length += 5

    print(f"{'слово':<{max_word_length}} | частота")

    print("-" * (max_word_length + 10))

    for word, count in top_words:
        print(f"{word:<{max_word_length}} | {count}")