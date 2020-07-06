class Stack:

    def __init__(self, *args) -> None:
        self.stack = list(*args)

    def size(self) -> int:
        """
        возвращает количество элементов в стеке.
        :return:[int] Count of elements in my stack
        """
        return len(self.stack)

    def isEmpty(self) -> bool:
        """
        Проверка стека на пустоту. True если пуст
        :return:[bool] True/False
        """
        if self.size() == 0:
            return True
        return False

    def push(self, value) -> None:
        """
        добавляет новый элемент на вершину стека. Метод ничего не возвращает
        :param value: New element
        :return:[None]
        """
        self.stack.insert(0, value)

    def peek(self):
        """
        возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        :return: The first element. Don't change my stack
        """
        return self.stack[0]

    def pop(self):
        """
        удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        :return: The first element and delete one from my stack
        """
        self.stack.pop(0)
        if not self.isEmpty():
            return self.stack[0]


def delete_from_2_stacks(stack_1, stack_2):
    stack_1.pop()
    stack_2.pop()


def first_check(stack, temp_stack):
    """
    Check: 1) Empty; 2) Size; 3) Closed bracket
    else: add the peek to temp_stack
    :param stack: original stack
    :param temp_stack: temporary stack
    :return: [None]
    """
    if stack.isEmpty():
        print('Стек пуст')
        exit()
    elif stack.size() % 2 != 0:
        print('Несбалансированно')
        exit()
    elif stack.peek() == ')' or stack.peek() == ']' or stack.peek() == '}':
        print('Несбалансированно')
        exit()
    else:
        temp_stack.push(stack.peek())
        stack.pop()


def check_couple(the_first_orig, the_first_temp):
    """
    Check couple closed and open brackets of the same type
    :param the_first_orig: the first element of orig
    :param the_first_temp: the first element of temp
    :return: [bool]
    """
    if the_first_orig == ')' and the_first_temp == '(':
        return True
    elif the_first_orig == ']' and the_first_temp == '[':
        return True
    elif the_first_orig == '}' and the_first_temp == '{':
        return True
    else:
        return False


def checking(orig_stack, temp_stack):
    if orig_stack.isEmpty() and temp_stack.isEmpty():
        print('Сбалансированно')
        exit()
    elif orig_stack.isEmpty() and not temp_stack.isEmpty():
        print('Несбалансированно')
        exit()
    elif temp_stack.isEmpty():
        add_to_temp(orig_stack, temp_stack)


def add_to_temp(orig_stack, temp_stack):
    temp_stack.push(orig_stack.peek())
    orig_stack.pop()
    if orig_stack.isEmpty():
        print('Несбалансированно')
        exit()


def delete(orig_stack, temp_stack):
    while check_couple(orig_stack.peek(), temp_stack.peek()):
        delete_from_2_stacks(orig_stack, temp_stack)
        checking(orig_stack, temp_stack)
    add_to_temp(orig_stack, temp_stack)


if __name__=='__main__':
    brackets_line = '[([])((([[[]]])))]{()}'
    temporary_stack = Stack()
    original_stack = Stack(list(brackets_line))

    first_check(original_stack, temporary_stack)
    while True:
        # save_to_temp_stack(original_stack, temporary_stack)
        delete(original_stack, temporary_stack)