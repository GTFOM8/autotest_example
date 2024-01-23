import fitz


class PDFPage:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf_and_convert_to_dict(self, pdf_path):
        """ Функция, читающая PDF-файл и выводящая его информацию в виде словаря
         Эта функция открывает PDF-файл, указанный в `pdf_path`, и извлекает из него текст.
    Затем текст преобразуется в словарь, где каждая пара ключ-значение получается из строки, содержащей двоеточие.
    Пары ключ-значение выводятся на экран.

         :param pdf_path: Путь к PDF-файлу, который необходимо прочитать.
         """
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()

            # Преобразование текста в словарь
            data_dict = {}
            for line in text.split('\n'):
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    data_dict[key.strip()] = value.strip()

            # Вывод содержимого словаря
            if data_dict:
                for key, value in data_dict.items():
                    print(f"{key}: {value}")
        except Exception as e:
            print(f"Возникла ошибка при чтении файла: {e}")


