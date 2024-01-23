from src.application import Application
from loguru import logger


def test_read_pdf_file(app: Application):
    logger.info("Шаг 1: Преобразовать информацию из PDF")
    app.pdf.read_pdf_and_convert_to_dict(pdf_path='test_task.pdf')
