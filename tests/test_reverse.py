from pathlib import Path
from hexlet_pytest.example import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

# тестируем функцию process(), которая как-то обрабатывает файл
def test_process():
    before_txt = read_file('before.txt')
    expected = read_file('result.txt')
    actual = reverse(before_txt)

    assert actual == expected
    print('OK!')