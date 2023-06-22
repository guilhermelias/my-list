from flask import Flask
from ViewModel.ListViewModel import ListViewModel

app = Flask(__name__)

class ListController:

    @app.route("/lista/")
    def create_list(self, list):
        list_view_model = ListViewModel(list)
        return print(list_view_model.name)
