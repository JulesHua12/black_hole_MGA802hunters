# Exemple ultra-simplifié de ce qu'il y aura dans main.py
from astro_module.data_handler import AstroFetcher, SignalCleaner
from astro_module.detector import AnomalyDetector
from astro_module.visualizer import AstroPlotter

# 1. Interaction utilisateur
target_id = input("Entrez l'identifiant de l'astre (ex: KIC 119584781) : ")

# 2. Maxence fait le travail
fetcher = AstroFetcher(target_id)
raw_data = fetcher.download_data()
clean_data = SignalCleaner(raw_data).remove_noise()

# 3. Jules fait le travail
detector = AnomalyDetector(clean_data)
anomalies = detector.find_anomalies()

# 4. Alexandre affiche le tout
plotter = AstroPlotter(raw_data, clean_data, anomalies)
plotter.show_results()
