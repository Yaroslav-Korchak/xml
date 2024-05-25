"""Условие задачи
Вам дан xml-файл с новостями. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.

Приведение к нижнему регистру не требуется.

В результате корректного выполнения задания будет выведен следующий результат:

1
['туристов', 'компании', 'Wilderness', 'странах', 'туризма', 'которые', 'африканских', 'туристы', 'является', 'природы']"""

import xml.etree.ElementTree as ET
from collections import Counter

def read_xml_file():
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    items = root.findall('.//item/description')
    texts = ' '.join(item.text for item in items if item.text)
    words = texts.split()
    long_words = [word for word in words if len(word) > 6]
    word_counts = Counter(long_words)
    top_10_words = [word for word, _ in word_counts.most_common(10)]
    return top_10_words

top_words = read_xml_file()
print(top_words)