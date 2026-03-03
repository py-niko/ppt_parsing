import os
import shutil


def destination_copy(matches):
    if not matches:
        print("Файл не найден.")

    else:
        destination = input("Куда копировать?\n>> ")
        print(f"Копирую файлы в {destination}")

        for file in matches:

            file_name = file.split(os.path.sep)[-1]
            dst_file_name = os.path.join(destination, file_name)

            count = 2
            while os.path.exists(dst_file_name):
                dst_file_name = os.path.join(destination, file_name.replace(".", f"({count}).", 1))

                count += 1

            shutil.copy2(file, dst_file_name)

            print("Копирование завершено!")
            return destination
