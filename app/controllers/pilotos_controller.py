from flask import request

from app.models.piloto_model import PilotoModel


class PilotosController:
    @staticmethod
    def criar_piloto():
        payload = request.get_json(silent=True) or {}
        nome = payload.get("nome")
        numero_kart = payload.get("numero_kart")
        equipe = payload.get("equipe")

        if not nome or not isinstance(numero_kart, int):
            return {
                "erro": "Dados inválidos. Envie 'nome' (texto) e 'numero_kart' (inteiro)."
            }, 400

        novo_id = PilotoModel.create(nome=nome, numero_kart=numero_kart, equipe=equipe)
        return {"mensagem": "Piloto cadastrado com sucesso.", "id": novo_id}, 201

    @staticmethod
    def listar_pilotos():
        pilotos = PilotoModel.list_all()
        return {"pilotos": pilotos}, 200

    @staticmethod
    def buscar_piloto(piloto_id):
        piloto = PilotoModel.get_by_id(piloto_id)
        if not piloto:
            return {"erro": "Piloto não encontrado."}, 404
        return piloto, 200

    @staticmethod
    def remover_piloto(piloto_id):
        removed = PilotoModel.delete(piloto_id)
        if not removed:
            return {"erro": "Piloto não encontrado."}, 404
        return {"mensagem": "Piloto removido com sucesso."}, 200
