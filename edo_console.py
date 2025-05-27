# Эмуляция электронного документооборота

class Document:
    statuses = ["Создан", "На согласовании", "Согласован"]

    def __init__(self, title):
        self.title = title
        self.status_index = 0

    def get_status(self):
        return self.statuses[self.status_index]

    def advance_status(self):
        if self.status_index < len(self.statuses) - 1:
            self.status_index += 1
            print(f"Документ '{self.title}' переведён в статус: {self.get_status()}")
        else:
            print(f"Документ '{self.title}' уже имеет финальный статус: {self.get_status()}")


def main():
    documents = []

    while True:
        print("\n--- Меню ---")
        print("1. Добавить документ")
        print("2. Показать все документы")
        print("3. Перевести документ в следующий статус")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название документа: ")
            documents.append(Document(title))
            print(f"Документ '{title}' добавлен.")

        elif choice == "2":
            if not documents:
                print("Документов пока нет.")
            else:
                for i, doc in enumerate(documents):
                    print(f"{i + 1}. {doc.title} — {doc.get_status()}")

        elif choice == "3":
            if not documents:
                print("Документов пока нет.")
            else:
                for i, doc in enumerate(documents):
                    print(f"{i + 1}. {doc.title} — {doc.get_status()}")
                try:
                    index = int(input("Введите номер документа: ")) - 1
                    documents[index].advance_status()
                except (ValueError, IndexError):
                    print("Неверный номер документа.")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
