from pandas import DataFrame, read_csv, merge, to_datetime
from os import path

COMMA = ','
DATA_DIRECTORY = path.join('datasets', 'data')


def load_apartments(remove_missing=True) -> DataFrame:
    """
    :param remove_missing:
    :return:
    """
    apartments_path = path.join(DATA_DIRECTORY, 'apartments.csv')
    dataset = read_csv(apartments_path, sep=COMMA)
    return dataset.dropna() if remove_missing else dataset


def load_covid(join_with_mcr: bool, join_with_bml: bool, remove_missing=True) -> DataFrame:
    """
    :param join_with_mcr:
    :param join_with_bml:
    :param remove_missing:
    :return:
    """
    covid_path = path.join(DATA_DIRECTORY, 'covid.csv')
    mcr_path = path.join(DATA_DIRECTORY, 'MCR.csv')
    bml_path = path.join(DATA_DIRECTORY, 'BML.csv')
    date = 'Date'
    mcr_date = 'MCR:Date'
    bml_date = 'BML:Date'

    dataset = read_csv(covid_path, sep=COMMA)
    dataset[date] = to_datetime(dataset[date]).dt.date

    if join_with_mcr:
        mcr_dataset = read_csv(mcr_path, sep=COMMA)
        mcr_dataset[mcr_date] = to_datetime(mcr_dataset[mcr_date]).dt.date
        dataset = merge(dataset, mcr_dataset, how='left', left_on=date, right_on=mcr_date)
        dataset.drop([mcr_date], axis=1, inplace=True)

    if join_with_bml:
        bml_dataset = read_csv(bml_path, sep=COMMA)
        bml_dataset[bml_date] = to_datetime(bml_dataset[bml_date]).dt.date
        dataset = merge(dataset, bml_dataset, how='left', left_on=date, right_on=bml_date)
        dataset.drop([bml_date], axis=1, inplace=True)

    return dataset.dropna() if remove_missing else dataset
