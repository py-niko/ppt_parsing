import os
import time


def search_file(path, query):
    prompt = """Введите сколько часов назад был создан файл (примерно),
        или пустой ввод если любой временной промежуток.
        >> """

    time_stamp = int(input(prompt) or 0) * 3600
    time_now = time.time()
    matches = []

    for address, dirs, files in os.walk(path):

        for file in files:
            if query in file:
                full_path = os.path.join(address, file)

                if os.path.islink(full_path):
                    continue

                if time_stamp:
                    if time_now - os.path.getctime(full_path) < time_stamp:
                        matches.append(full_path)

                else:
                    matches.append(full_path)

    return matches
