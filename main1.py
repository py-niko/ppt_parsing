import search
import validation
import archiv


def file_result():
    query = input("Что ищем?\n>> ")

    path = str(input('Укажите директорию поиска\n>> '))
    research_result = search.search_file(path, query)
    destination = validation.destination_copy(research_result)
    archiv.arhive(destination)


if __name__ == '__main__':
    file_result()
