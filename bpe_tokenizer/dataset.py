from .dataset_loader import DatasetLoader

class Dataset:
    def __init__(self, dataset_ref="breandan/french-reddit-discussion", download_dir="data", max_length=None):
        """
        Initialise la classe Dataset.
        :param dataset_ref: Référence au Dataset.
        :param download_dir: Dossier dans lequel télécharger le Dataset.
        """

        self.raw_data = DatasetLoader(dataset_ref, download_dir).load()
        self.max_length = max_length
        self.data = None

    def preprocess(self):
        """
        Prétraite le Dataset en supprimant les colonnes et lignes inutiles.
        :return: Dataset prétraité.
        """

        text_only = self.raw_data["utt"]

        text_only = text_only[text_only.str.strip() != ""]
        text_only = text_only[text_only.str.len() > 5]

        text_only = text_only.str.lower()

        text_only = text_only.str.replace(r"[\u00A0\u202F\u2009]", " ", regex=True)

        text_only = text_only.str.replace(r"[\U00010000-\U0010ffff]", "", regex=True)

        text_only = text_only.str.replace(r"http\S+|www\S+|https\S+", "", regex=True)

        text_only = text_only.str.replace(r"[^a-zA-Z0-9\sàâäçéèêëîïôöùûüÿœæ.,!?;:()'\"-]", "", regex=True)

        self.data = text_only.to_list()

        if self.max_length is not None:
            self.data = self.data[: self.max_length]
