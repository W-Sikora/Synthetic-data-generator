from pandas import DataFrame
from datasets.pasta import get_dataset

from datasets.data_loader import load_apartments, load_covid


def generate_apartments() -> DataFrame:
    base_data = load_apartments()
    pass


def generate_covid() -> DataFrame:
    base_data = load_covid(False, False)
    pass


def generate_pasta(size: int) -> DataFrame:
    return get_dataset(size)
