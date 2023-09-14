import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

f =  open("raw.txt", "r", encoding="utf-8")
text = f.read()

phrasal_verbs = []
max_chunk_length = 1000000
chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]


for i in chunks:
    doc = nlp(i)

    # Извлеките наречия из документа
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]

    # Выведите список наречий
    for ii in adverbs:
        phrasal_verbs.append(ii)



# Подсчитываем количество совпадений для каждого элемента
counts = Counter(phrasal_verbs)

# Сортируем элементы по количеству совпадений (по возрастанию)
sorted_items = sorted(counts.items(), key=lambda x: x[1])

# Выводим отсортированные элементы и их количества
for item, count in sorted_items:
    print(f"{item}: {count}")


print(len(phrasal_verbs))
