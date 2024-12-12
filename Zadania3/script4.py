# 4. Zaimplementowac algorytm Aho-Corasick


class Node:
    def __init__(self):
        self.next = {}      # słownik:  char: Node
        self.output = []    # znalezione słowa: ["asd", "hasd"]
        self.fail = None    # link do najdłuższego prefixu


class AhoCorasick:
    def __init__(self, words):
        # utworzenie drzewa
        self.words = words
        self.root = Node()

        for word in words:

            node = self.root

            for char in word:
                # jak istnieje odpowiedni stan to do niego przechodzimy a jak nie to tworzymy nowy
                node = node.next.setdefault(char, Node())

            # przypisujemy wyjście dla końca gałęzi
            node.output.append(word)

        queue = []

        for node in self.root.next.values():

            queue.append(node)
            node.fail = self.root

        while queue:

            current_node = queue.pop(0)

            for key, node in current_node.next.items():

                queue.append(node)

                # szukanie węzła z najdłuższym pokryciem suffixu z prefixem
                fail_node = current_node.fail
                while fail_node and key not in fail_node.next:  # dopóki nie znajdziemy znaku w gałęzi
                    fail_node = fail_node.fail  # cofamy się do fail

                node.fail = fail_node.next[key] if fail_node else self.root

                # dodajemy wyjścia
                node.output += node.fail.output

    def search_words(self, text):

        result = {word: [] for word in self.words}
        current_node = self.root

        for i, char in enumerate(text):

            while current_node and char not in current_node.next:   # jeśli nie ma odpowiedniego linku idzie do fail
                current_node = current_node.fail

            if not current_node:        # jesli fail jest None, zaczynamy od początku
                current_node = self.root
                continue

            current_node = current_node.next[char]

            # dopisywanie indeksów do wyników
            for word in current_node.output:
                result[word].append(i - len(word) + 1)

        return result


if __name__ == "__main__":
    input_words = ["hey", "a", "ab", "ah"]
    input_text = "heyabhea abahey"
    test = AhoCorasick(input_words)
    print(test.search_words(input_text))