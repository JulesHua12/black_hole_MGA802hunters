from astro_module.data_handler import AstroFetcher, SignalCleaner

# 1. Define the target star (Kepler-10)
target = "KIC 11904151"

# 2. Maxence's job: Fetch the data
fetcher = AstroFetcher(target)
raw_data = fetcher.download_data(mission='Kepler')

# 3. Maxence's job: Clean the data
cleaner = SignalCleaner(raw_data)
clean_data = cleaner.process_data()

# 4. Maxence's job: Save the data locally for Jules
file_name = f"{target}_cleaned.csv"
cleaner.save_to_csv(clean_data, filename=file_name)

# 5. Quick verification (Sanity check)
print("\nHere are the first 5 rows of the dataset ready for the AI:")
print(clean_data.head())