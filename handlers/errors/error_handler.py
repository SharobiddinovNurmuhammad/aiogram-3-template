import logging
from aiogram.exceptions import *

from loader import dp

@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Istisnolarni ishlovchi. Aiogram vazifalari ichidagi barcha istisnolarni ushlaydi.
    :param dispatcher:
    :param yangilanish:
    :param istisno:
    :return: stdout logging
    """
    exception_list = [TelegramServerError, TelegramUnauthorizedError, TelegramConflictError, TelegramNetworkError,
                      TelegramAPIError, TelegramForbiddenError, TelegramMethod, TelegramNotFound, TelegramRetryAfter,
                      TelegramBadRequest, TelegramMigrateToChat, TelegramType, TelegramEntityTooLarge,
                      RestartingTelegram,
                      UnsupportedKeywordArgument, ClientDecodeError, AiogramError, DetailedAiogramError,
                      SceneException, CallbackAnswerException]
    for exc in exception_list:
        if isinstance(exception, exc):
            logging.exception(f'TelegramUnauthorizedError: {exception}')
            return True

    logging.exception(f'Update: {update} \n{exception}')