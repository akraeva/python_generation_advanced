# 18. Итоговая работа на файлы
"""
Этот модуль содержит дополнительные задачи по изученным темам.
Они помогут еще раз закрепить ваши знания, углубить понимание
ключевых концепций и убедиться, что вы освоили материал.
"""

# 18.1 Итоговая работа


def m_18_1_1():  # Количество строк в файле
    file_name = input()
    with open(file_name, encoding="utf-8") as file:
        print(len(file.readlines()))


def m_18_1_2():  # Суммарная стоимость
    file_name = "ledger.txt"  # <= "data/ledger.txt" для тестов
    with open(file_name, encoding="utf-8") as file:
        print(f'${sum(int(row.strip("$")) for row in file)}')


def m_18_1_3():  # Goooood students
    file_name = "grades.txt"  # <= "data/grades.txt" для тестов
    with open(file_name, encoding="utf-8") as file:
        print(
            sum(
                1
                for row in file
                if all(int(x) >= 65 for x in filter(lambda x: x.isdigit(), row.split()))
            )
        )


def m_18_1_4():  # Самое длинное слово в файле
    file_name = "words.txt"  # <= "data/words.txt" для тестов
    with open(file_name, encoding="utf-8") as file:
        max_len = max(len(max(line.strip().split(), key=len)) for line in file)
        file.seek(0)
        print(
            *(
                word
                for line in file
                for word in (filter(lambda w: len(w) == max_len, line.strip().split()))
            ),
            sep="\n",
        )


def m_18_1_5():  # Tail of a File
    file_name = input()  # <= "data/test_file.txt" для тестов
    with open(file_name, encoding="utf-8") as file:
        lines = file.readlines()
        print(*lines[-10:], sep="")


def m_18_1_6():  # Forbidden words
    def cheked(word):
        result = word.lower()
        for bad in forbidden:
            while bad in result:
                result = result.replace(bad, "*" * len(bad))
        return "".join(w if r != "*" else r for w, r in zip(word, result))

    # "data/data-2.txt",  "data/beegeek.txt",   "data/stepik.txt" для тестов
    forbidden_words = "forbidden_words.txt"  # <= "data/forbidden_words.txt" для тестов
    with open(forbidden_words, encoding="utf-8") as file:
        forbidden = file.read().split()

    file_name = "data/beegeek.txt"  # input()
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            print(cheked(line.strip("\n")))


def m_18_1_7():  #
    def translit(text):
        translit_text = ""
        for ch in text:
            if ch.lower() in translit_dict:
                translit_ch = translit_dict[ch.lower()]
                translit_text += (
                    translit_ch.capitalize() if ch.isupper() else translit_ch
                )
            else:
                translit_text += ch
        return translit_text

    translit_dict = {
        "а": "a",
        "к": "k",
        "х": "h",
        "б": "b",
        "л": "l",
        "ц": "c",
        "в": "v",
        "м": "m",
        "ч": "ch",
        "г": "g",
        "н": "n",
        "ш": "sh",
        "д": "d",
        "о": "o",
        "щ": "shh",
        "е": "e",
        "п": "p",
        "ъ": "*",
        "ё": "jo",
        "р": "r",
        "ы": "y",
        "ж": "zh",
        "с": "s",
        "ь": "'",
        "з": "z",
        "т": "t",
        "э": "je",
        "и": "i",
        "у": "u",
        "ю": "ju",
        "й": "j",
        "ф": "f",
        "я": "ya",
    }

    file_name = "cyrillic.txt"  # "data/cyrillic.txt" для тестов
    with open(file_name, encoding="utf-8") as input_file, open(
        "transliteration.txt", "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            output_file.write(translit(line))


def m_18_1_8():  # Пропущенные комменты
    pass


file_name = input()  # "data/test_file_18_1_8.txt" для тестов
with open(file_name, encoding="utf-8") as file:
    lines = file.readlines()
result = []
for n, line in enumerate(lines):
    if line.startswith("def ") and (n == 0 or not lines[n - 1].startswith("#")):
        result.append(line.strip()[4 : line.index("(")])
print("\n".join(result) if result else "Best Programming Team")
