import json

from app.models.corrida_model import CorridaModel
from app.services.corrida_service import CorridaService


class CorridasController:
    @staticmethod
    def simular_corrida():
        resultado, erro = CorridaService.simular_corrida()
        if erro:
            return {"erro": erro}, 400
        return resultado, 201

    @staticmethod
    def listar_corridas():
        corridas = CorridaModel.list_all()
        for corrida in corridas:
            corrida["resultado"] = json.loads(corrida.pop("resultado_json"))
        return {"corridas": corridas}, 200
