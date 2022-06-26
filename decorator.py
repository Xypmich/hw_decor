from datetime import datetime

def func_log(path):
    def _func_log(old_function):
        def new_function(*args, **kwargs):
            start = datetime.now()
            result = old_function(*args, **kwargs)
            log = {
                'Дата': start.strftime('%d.%m.20%y'),
                'Время': start.strftime('%H:%M:%S'),
                'Имя функции': old_function.__name__,
                'Аргументы': [args, kwargs],
                'Результат функции': result
            }
            with open(path, 'a', encoding='utf-8') as f:
                f.write(str(log) + '\n')

            return result
        return new_function
    return _func_log

