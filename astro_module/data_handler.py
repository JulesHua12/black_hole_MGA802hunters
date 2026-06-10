import warnings
warnings.filterwarnings('ignore') # Masque les avertissements inoffensifs
import lightkurve as lk
import pandas as pd
import warnings
import os

# Hide harmless warnings from the lightkurve library
warnings.filterwarnings('ignore')


class AstroFetcher:
    """
    Class responsible for searching and downloading light curves
    from public NASA archives (Kepler/TESS).
    """

    def __init__(self, target_id):
        self.target_id = target_id

    def download_data(self, mission='Kepler'):
        """
        Searches and downloads the data for the targeted celestial object.
        """
        print(f"Searching for data for target {self.target_id} (Mission: {mission})...")

        search_result = lk.search_lightcurve(self.target_id, mission=mission)

        if len(search_result) == 0:
            raise ValueError(f"No data found for {self.target_id}. Please check the ID.")

        print(f"Data found. Downloading the first available observation set...")
        return search_result[0].download()


class SignalCleaner:
    """
    Class responsible for preprocessing (cleaning, removing outliers,
    and handling observation gaps) to prepare the data for the algorithm.
    """

    def __init__(self, raw_lightcurve):
        self.lc = raw_lightcurve

    def process_data(self):
        """
        Cleans the light curve and converts it into a Pandas DataFrame
        to facilitate Machine Learning operations.
        """
        print("🧹 Cleaning data...")

        # 1. Remove missing values (NaN)
        clean_lc = self.lc.remove_nans()

        # 2. Flatten the curve (remove long-term trend) and remove extreme outliers
        flat_lc = clean_lc.flatten(window_length=401).remove_outliers(sigma=5)

        # 3. Convert to a Pandas DataFrame
        df = pd.DataFrame({
            'time': flat_lc.time.value,
            'flux': flat_lc.flux.value
        })

        print("Cleaning complete. Data is ready for analysis.")
        return df

    def save_to_csv(self, df, filename="clean_data.csv"):
        """
        Saves the Pandas DataFrame to a CSV file on the local machine.
        """
        # 1. Ensure the "data/processed" directory exists
        save_folder = os.path.join("data", "processed")
        os.makedirs(save_folder, exist_ok=True)

        # 2. Create the full file path
        full_path = os.path.join(save_folder, filename)

        # 3. Save the dataframe (without the index column)
        df.to_csv(full_path, index=False)
        print(f"File successfully saved at: {full_path}")