from numpy import round
from numpy.random import choice, randint
from pandas import DataFrame

from datasets.util.dictionary_utils import keys_to_list
from datasets.util.rounding_mode import NEAREST_TEN, NEAREST_HUNDRED

MIN_COOKING_TIME = 240
MAX_COOKING_TIME = 1140

MIN_AMOUNT_OF_WATER = 90
MAX_AMOUNT_OF_WATER = 6200

MIN_AMOUNT_OF_PASTA = 50
MAX_AMOUNT_OF_PASTA = 500

PASTA = {
    'Farfalle': 780,
    'Fusilli': 660,
    'Penne': 600,
    'Rigatoni': 720,
    'Spaghetti': 480,
    'Tagliatelle': 360
}

SALTED = {
    'salted': 1,
    'unsalted': 0
}

STIRRED = {
    'stirred': 1,
    'unstirred': 0
}

COVERED = {
    'covered': 1,
    'uncovered': 0
}

DEGREE_OF_DONENESS = [
    'undercooked',
    'al dente',
    'overcooked'
]

THRESHOLD = 35


def get_dataset(size: int, f=None) -> DataFrame:
    """
    :param f:
    :param size:
    :return: DataFrame (synthetic type; cook time; amount of water, amount of synthetic; salted; stirred; )
    """

    def calculate_score(measurements: dict, index: int, f=None) -> float:
        """
        :param f:
        :param measurements:
        :param index:
        :return:
        """
        pasta_type = measurements['pasta type'][index]
        cook_time = measurements['cook time'][index]
        amount_of_water = measurements['amount of water'][index]
        amount_of_pasta = measurements['amount of pasta'][index]
        salted = SALTED[measurements['salted'][index]]
        stirred = STIRRED[measurements['stirred'][index]]
        covered = COVERED[measurements['covered'][index]]

        proper_cook_time = PASTA[pasta_type]

        if f is not None:
            return f(measurements, index)

        return 1 + (covered / 3 + stirred / 8 + salted / 21) * amount_of_water / (10 * amount_of_pasta) * (
                cook_time - proper_cook_time)

    def assign_to_category(score: float) -> str:
        """
        :param score:
        :return:
        """
        if score < - THRESHOLD:
            return DEGREE_OF_DONENESS[0]
        elif score <= THRESHOLD:
            return DEGREE_OF_DONENESS[1]
        else:
            return DEGREE_OF_DONENESS[2]

    assert size > 0, 'Size of the dataset must be greater than 0'

    data = {
        'pasta type': choice(keys_to_list(PASTA), size),
        'cook time': randint(MIN_COOKING_TIME, MAX_COOKING_TIME, size),
        'amount of water': round(randint(MIN_AMOUNT_OF_WATER, MAX_AMOUNT_OF_WATER, size), NEAREST_HUNDRED),
        'amount of pasta': round(randint(MIN_AMOUNT_OF_PASTA, MAX_AMOUNT_OF_PASTA, size), NEAREST_TEN),
        'salted': choice(keys_to_list(SALTED), size),
        'stirred': choice(keys_to_list(STIRRED), size),
        'covered': choice(keys_to_list(COVERED), size)
    }

    scores = [calculate_score(data, index, f) for index in range(size)]

    data['doneness'] = [assign_to_category(score) for score in scores]

    return DataFrame(data)
