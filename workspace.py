from datasets.data_loader import load_apartments, load_covid
from datasets.data_generator import generate_pasta
from datasets.util.dataframe import analyze_dataset
from datasets.util.distribution_matcher import match_distribution
import matplotlib.pyplot as plt
import scipy as sc
# from pandas_profiling import ProfileReport

# pasta_dataset = generate_pasta(100)
# analyze_dataset(pasta_dataset)

# apartments_dataset = load_apartments()
# analyze_dataset(apartments_dataset)
# areas = apartments_dataset['Apartment area']
# print(match_distribution(areas))
#
# plt.hist(areas)
# plt.show()

# covid_dataset = load_covid(join_with_mcr=True, join_with_bml=True, remove_missing=True)
# analyze_dataset(covid_dataset)
# plt.plot(covid_dataset['Date'], covid_dataset['MCR:Open'], '.')
# plt.show()
# plt.plot(covid_dataset['Date'], covid_dataset['Newcases'], '.')
# plt.show()
# profile = ProfileReport(covid_dataset, title='report')
# profile.to_file('report.html')
