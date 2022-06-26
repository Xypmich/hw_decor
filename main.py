from decorator import func_log
from pprint import pprint

@func_log('logs/func_log.log')
def flat_generator(raw_list):
    count_list = 0
    count_list_item = 0
    while count_list < len(raw_list):
        yield raw_list[count_list][count_list_item]
        count_list_item += 1
        if count_list_item == len(raw_list[count_list]):
            count_list += 1
            count_list_item = 0


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)
    with open('logs/func_log.log', 'r', encoding='utf-8') as f:
        text = f.read().split('\n')
        pprint(text)
