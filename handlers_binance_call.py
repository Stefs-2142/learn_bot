from binance_utils import BinanceClient

binance_client = BinanceClient()


def get_average_price(update, context):
    """Проверяем актуальный курс заданной пары."""

    user_input = context.args
    update.message.reply_text('Загружаю.')
    result = binance_client.get_average_price((user_input[0], user_input[1]))
    update.message.reply_text(result)


def get_all_open_orders(update, context):
    """Получаем все открытыие ореда."""
    open_orders = binance_client.get_all_open_orders()
    update.message.reply_text(open_orders)
    if open_orders is not None:
        update.message.reply_text(open_orders)
        return
    update.message.reply_text('Нет открытых ордеров.')


def get_balance(update, context):
    """Получаем баланс пользователя на бирже Binance."""
    balance = binance_client.get_balance()
    update.message.reply_text(balance)


def get_trade_history(update, context):
    """"Получаем историю торгов по заданному тикеру."""
    user_input = context.args
    result = binance_client.get_trade_history(user_input[0], user_input[1])
    update.message.reply_text(result)
