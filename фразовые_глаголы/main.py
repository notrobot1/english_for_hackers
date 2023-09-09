import spacy
from collections import Counter
# Загрузите модель
nlp = spacy.load("en_core_web_sm")  # Используйте правильное название модели для вашего языка

# Найдите фразовые глаголы
phrasal_verbs = []
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()


max_chunk_length = 1000000
chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]



for i in chunks:

    # Обработайте текст с помощью spaCy
    doc = nlp(i)



    for token in doc:
        if "prt" in [child.dep_ for child in token.children]:  # Проверьте, есть ли зависимость "prt" (частицы) у текущего токена
            phrasal_verb = token.text + " " + " ".join([child.text for child in token.children if child.dep_ == "prt"])
            phrasal_verbs.append(phrasal_verb)



# Подсчитываем количество совпадений для каждого элемента
counts = Counter(phrasal_verbs)

# Сортируем элементы по количеству совпадений (по возрастанию)
sorted_items = sorted(counts.items(), key=lambda x: x[1])

# Выводим отсортированные элементы и их количества
for item, count in sorted_items:
    print(f"{item}: {count}")


print(len(phrasal_verbs))
