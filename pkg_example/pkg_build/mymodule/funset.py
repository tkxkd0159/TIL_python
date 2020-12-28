"""PYTHON FILE DOCSTRING TEST"""

import os

def func_annotation(*args: "unlimit arguments", num: int = 3, **kwargs: "unlimit keyword-values") -> None:
    """
    Test function annotation

    Returns:
        None
    """
    keys, values = [], []
    for key, value in kwargs.items():
        keys.append(key)
        values.append(value)

    print(args, num)
    print("key : ", keys, "value : ", values)
    return None

def logging_decorator(func):
    def wrapper_function(*args, **kwargs):
        print(func.__name__ + " was called")
        print("결과 :", func(*args, **kwargs))
    return wrapper_function

MODULENAME = 'Practice module'

@logging_decorator
def square_number(var):
    return var**2


@logging_decorator
def add_number(var, var2=0):
    return var+var2


@logging_decorator
def add_numbers(*args, **kwargs):
    if args != ():
        num_list = [ls for ls in args]
    else :
        num_list = []
    if kwargs != {}:
        num_list2 = [ls for ls in kwargs.values()]
    else :
        num_list2 = []

    newlist = num_list + num_list2
    return sum(newlist[:])

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def multiadd(self):
        res = 0
        numlist = []
        tempnum = ""
        addlist = input("Enter your number and add space after number\n")
        for seq in addlist:
            tempnum += seq
            if seq == " ":
                if tempnum == " ":
                    continue
                numlist.append(int(tempnum))
                tempnum = ""
        if tempnum != "":
            numlist.append(int(tempnum))
        for add in numlist:
            res += add
        return res

class UpgradeCalculator(Calculator):
    def sub(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

class TestAssert(object):
    def test_one(self):
        var = "this"
        assert 'a' in var
        return var

    def test_two(self):
        var = "hello"
        assert hasattr(var, 'check')

class Filemod:
    def file_io(self):
        print("="*50, "\nSelect mode \n\n 1: Generate new file \
        2: Modify existing file ", "\n", "="*50)
        w_type = input()


        if w_type == '1':
            file_name = input("Enter a file name with *.txt : ")
            txtdata = []
            while True:
                txtdata.append(input("Enter your data(N) : "))
                if not txtdata[-1]:
                    break
                txtdata.append('\n')
            txtdata.pop()
            with open(file_name, 'w') as file_:
                for i in txtdata:
                    file_.write(i)

        if w_type == '2':
            file_name = input("Enter a file name with *.txt : ")
            txtdata = []
            while True:
                txtdata.append(input("Enter your data(M) : "))
                if not txtdata[-1]:
                    break
                txtdata.append('\n')
            txtdata.pop()
            with open(file_name, 'a') as file_:
                file_.seek(0, 2)
                file_.writelines(txtdata)

    def word_sw(self, src, dst):
        file_name = input("Enter a file name with *.txt : ")
        with open(file_name, 'r+') as file_:
            tmp = file_.read()
            tmp = tmp.replace(src, dst)
            print(tmp)
            file_.seek(0, 0)
            file_.writelines(tmp)

class SearchMod:
    def __init__(self, savpath):
        self.savpath = savpath

    def dir_search(self, path, *args):
        try:
            init = 0
            if args != ():
                init = 1
            if init == 0:
                if args == ():
                    os.chdir(self.savpath)
                    file_ = open("dirlist_old.txt", 'w')
                    file_.close()
                    file_ = open("dirlist_old.txt", 'a')
            if init == 1:
                file_ = open("dirlist_old.txt", 'a')
            filenames = os.listdir(path) # 'path' is starting path of search

            for tmp in filenames:
                full_name = os.path.join(path, tmp)
                file_.write(full_name)
                file_.write("\n")
                # if os.path.splitext(full_name)[1] !='':
                #     print("File extension is ",os.path.splitext(full_name)[-1])

                if os.path.isdir(full_name):
                    self.dir_search(full_name, 1)
        except PermissionError:
            pass

    def dir_search2(self, path):
        try:
            os.chdir(self.savpath)
            with open("dirlist.txt", 'w') as file_:
                for (paths, subdir, files) in os.walk(path):
                    # file_.write(paths)
                    # file_.write('\n')
                    for piece in files:
                        full_name = os.path.join(paths, piece)
                        if piece == []:
                            continue
                        file_.write(full_name)
                        file_.write("\n")
                    for piece2 in subdir:
                        full_dir = os.path.join(paths, piece2)
                        if piece2 == []:
                            continue
                        file_.write(full_dir)
                        file_.write("\n")
        except PermissionError:
            pass
