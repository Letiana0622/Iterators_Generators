#1 - Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
# возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в
# коде ниже также должна отработать без ошибок.
#2 - Доработать функцию flat_generator, Должен получиться генератор, который принимает список списков и возвращает
# их плоское представление. Функция test в коде ниже также должна отработать без ошибок.
#3.* Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.
# Шаблон и тест в коде ниже:
#4 Написать генератор аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности.

#111111111111111111111111111111
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

#22222222222222222222222222
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

#33333333333333333333333333333
final_list = []

def reemoveNestings(values_):
    for i in values_:
        if type(i) == list:
            reemoveNestings(i)
        else:
            final_list.append(i)
    return final_list

class FlatIterator_:

    def __init__(self, values_):
        self.values_ = values_

    def __iter__(self):
        self.new_list = reemoveNestings(self.values_)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator_(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator_(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

#444444444444444444444444444444
import types

def flat_generator_(values_):
    new_list = reemoveNestings(values_)
    cursor = 0
    while cursor != len(new_list):
        yield new_list[cursor]
        cursor += 1

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator_(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()

    # values = [
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]

    # final_list = []
    #
    # values_ = [
    #     [['a'], ['b', 'c']],
    #     ['d', 'e', [['f'], 'h'], False],
    #     [1, 2, None, [[[[['!']]]]], []]
    # ]

    # print(reemovNestings(values_))

    # for item in FlatIterator(values):
    #     print(item)
    #
    # for item in FlatIterator_(values_):
    #     print(item)

    # for item in flat_generator(values):
    #    print(item)
    #
    # for item in flat_generator_(values_):
    #    print(item)
