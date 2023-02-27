import logging
import matplotlib.pyplot as plt
import os

#authored by Geovana Mosquera
def save_plot(
        folder_path: str,
        plot: plt,
        name: str = "plot",
        **kwargs
) -> bool:
    try:
        # TODO: Save Plots
        try:
            os.makedirs(folder_path)
        except Exception:
            logging.info(f"FOLDER PATH : {folder_path} : This folder was already created!")

        file_path = os.path.join(folder_path, name)
        plot.savefig(file_path)

        # TODO: print the location of saved plots
        logging.info(f"PLOT SAVED:\t{file_path}")
        return True

    except Exception:
        return False
