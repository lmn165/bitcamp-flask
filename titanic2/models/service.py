import pandas as pd

from titanic2.models.dataset import Dataset


class Service(object):
    data_set = Dataset()

    def new_model(self, payload) -> str:
        this = self.data_set
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
