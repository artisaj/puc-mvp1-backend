import json
import random
from datetime import datetime

from app.models.piloto_model import PilotoModel
from app.models.corrida_model import CorridaModel


class CorridaService:
    @staticmethod
    def simular_corrida():
        pilotos = PilotoModel.list_all()
        if len(pilotos) < 2:
            return None, "Cadastre pelo menos 2 pilotos para simular uma corrida."

        tempos = []
        for piloto in pilotos:
            tempo_total = round(random.uniform(55.0, 72.0), 3)
            tempos.append(
                {
                    "piloto_id": piloto["id"],
                    "nome": piloto["nome"],
                    "numero_kart": piloto["numero_kart"],
                    "tempo": tempo_total,
                }
            )

        ranking = sorted(tempos, key=lambda item: item["tempo"])
        for indice, item in enumerate(ranking, start=1):
            item["posicao"] = indice

        data_corrida = datetime.now().isoformat(timespec="seconds")
        corrida_id = CorridaModel.create(data_corrida, json.dumps(ranking, ensure_ascii=False))

        return {
            "corrida_id": corrida_id,
            "data_corrida": data_corrida,
            "ranking": ranking,
        }, None
