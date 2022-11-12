#1 - Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
# возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в
# коде ниже также должна отработать без ошибок.
#2 - Доработать функцию flat_generator, Должен получиться генератор, который принимает список списков и возвращает
# их плоское представление. Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, values):
        self.values = values

    def __iter__(self):
        self.new_list = sum(self.values, [])
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


import types


def flat_generator(values):
    new_list = sum(values, [])
    cursor = 0
    while cursor != len(new_list):
        yield new_list[cursor]
        cursor += 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    # test_1()
    test_2()

    # values = [
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]
    # for item in FlatIterator(values):
    #     print(item)
    #
    # for item in flat_generator(values):
    #    print(item)
