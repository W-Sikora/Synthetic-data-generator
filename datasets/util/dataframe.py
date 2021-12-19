from pandas import DataFrame


def analyze_dataset(dataset: DataFrame):
    print(f'{dataset.info()}\n{dataset.head()}')
