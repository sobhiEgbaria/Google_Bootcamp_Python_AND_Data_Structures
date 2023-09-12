from CS_day_6_solutions import *
import io
import os

def test_sumTwoIntegers():
    sys.argv = ['file', '2', '3']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    sumTwoIntegers()
    assert sys.stdout.getvalue() == '5\n'
    sys.stdout = old_stdout

def test_stringLength():
    sys.argv = ['file', 'Hello']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    stringLength()
    assert sys.stdout.getvalue() == '5\n'
    sys.stdout = old_stdout

def test_averageList():
    sys.argv = ['file', '1', '2', '3', '4', '5']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    averageList()
    assert sys.stdout.getvalue() == '3.0\n'
    sys.stdout = old_stdout

def test_checkPalindrome():
    # Test case where the result is True
    sys.argv = ['file', 'racecar']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    checkPalindrome()
    assert sys.stdout.getvalue() == 'True\n'
    
    # Test case where the result is False
    sys.argv = ['file', 'hello']
    sys.stdout = io.StringIO()
    checkPalindrome()
    assert sys.stdout.getvalue() == 'False\n'
    sys.stdout = old_stdout

def test_validateEmail():
    # Test case where the result is True
    sys.argv = ['file', 'myemail@example.com']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    validateEmail()
    assert sys.stdout.getvalue() == 'True\n'

    # Test case where the result is False
    sys.argv = ['file', '123@abc.com']
    sys.stdout = io.StringIO()
    validateEmail()
    assert sys.stdout.getvalue() == 'False\n'

    # Test case where the result is False
    sys.argv = ['file', 'abc@example']
    sys.stdout = io.StringIO()
    validateEmail()
    assert sys.stdout.getvalue() == 'False\n'
    sys.stdout = old_stdout



def test_encryptCaesarCipher():
    sys.argv = ['file', 'HELLO', '3']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    encryptCaesarCipher()
    assert sys.stdout.getvalue() == 'KHOOR\n'
    sys.stdout = old_stdout

def test_wordCounter():
    sys.argv = ['file', 'This is a simple sentence.']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    wordCounter()
    assert sys.stdout.getvalue() == '5\n'
    sys.stdout = old_stdout

def test_sortList():
    sys.argv = ['file', '5', '3', '9', '1', '6']
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    sortList()
    assert sys.stdout.getvalue() == '[1, 3, 5, 6, 9]\n'
    sys.stdout = old_stdout


# helper method to clean up created files
def clean_files(*filenames):
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def test_wordFrequencyCounter():
    input_file = 'test_input.txt'
    output_file = 'test_output.txt'
    with open(input_file, 'w') as file:
        file.write("apple apple banana apple cherry cherry cherry")

    wordFrequencyCounter(input_file, output_file)

    with open(output_file, 'r') as file:
        output = file.read()

    assert output == "apple: 3\ncherry: 3\nbanana: 1\n"
    clean_files(input_file, output_file)


def test_csvFileParsing():
    csv_file = 'test.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Alice', 'Biology', 'A'])
        writer.writerow(['Bob', 'Chemistry', 'B'])

    result = csvFileParsing(csv_file)
    assert result == [['Alice', 'Biology', 'A'], ['Bob', 'Chemistry', 'B']]

    clean_files(csv_file)


def test_logFileAnalysis():
    log_file = 'test.log'
    output_file = 'output.log'
    first = "Error 1, Timestamp 1, Machine 1"
    second = "Error 2, Timestamp 2, Machine 2"
    with open(log_file, 'w') as file:
        file.write("Error 1, Timestamp 1, Machine 1\nError 2, Timestamp 2, Machine 2")
        # file.write(first + '\n')
        # file.write('\n')
        # file.write(second)

    logFileAnalysis(log_file, output_file)

    with open(output_file, 'r') as file:
        output = file.readlines()

    assert output == ["('Error 1', ' Timestamp 1', ' Machine 1\\n')\n", "('Error 2', ' Timestamp 2', ' Machine 2')\n"]
    clean_files(log_file, output_file)


def test_wordSearchInFile():
    word_file = 'test.txt'
    with open(word_file, 'w') as file:
        file.write("apple\nbanana\napple\nbanana\napple")

    result = wordSearchInFile(word_file, "apple")
    assert result == [1, 3, 5]

    clean_files(word_file)


def test_replaceWordsInFile():
    input_file = 'test_input.txt'
    output_file = 'test_output.txt'
    with open(input_file, 'w') as file:
        file.write("apple apple banana apple cherry cherry cherry")

    replaceWordsInFile(input_file, output_file, "apple", "mango")

    with open(output_file, 'r') as file:
        output = file.read()

    assert output == "mango mango banana mango cherry cherry cherry"

    clean_files(input_file, output_file)

def run_all_tests():
    test_sumTwoIntegers()
    print("Passed test_sumTwoIntegers")

    test_stringLength()
    print("Passed test_stringLength")

    test_averageList()
    print("Passed test_averageList")

    test_checkPalindrome()
    print("Passed test_checkPalindrome")

    test_validateEmail()
    print("Passed test_validateEmail")

    test_encryptCaesarCipher()
    print("Passed test_encryptCaesarCipher")

    test_wordCounter()
    print("Passed test_wordCounter")

    test_sortList()
    print("Passed test_sortList")
    
    test_wordFrequencyCounter()
    print("Passed test_wordFrequencyCounter")

    test_csvFileParsing()
    print("Passed test_csvFileParsing")

    test_logFileAnalysis()
    print("Passed test_logFileAnalysis")

    test_wordSearchInFile()
    print("Passed test_wordSearchInFile")

    test_replaceWordsInFile()
    print("Passed test_replaceWordsInFile")


    print("Passed all tests!!!")

run_all_tests()
