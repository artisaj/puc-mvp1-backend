from flask import Blueprint

from app.controllers.corridas_controller import CorridasController

corridas_bp = Blueprint("corridas", __name__)


@corridas_bp.post("/corridas/simular")
def simular_corrida():
    """
    Simula uma corrida e salva o resultado.
    ---
    summary: Simula uma corrida
    tags:
      - Corridas
    produces:
      - application/json
    responses:
      201:
        description: Corrida simulada com sucesso.
        content:
          application/json:
            schema:
              type: object
              properties:
                corrida_id:
                  type: integer
                  example: 3
                data_corrida:
                  type: string
                  example: 2026-03-29T18:35:10
                ranking:
                  type: array
                  items:
                    type: object
                    properties:
                      piloto_id:
                        type: integer
                        example: 1
                      nome:
                        type: string
                        example: Ayrton Lima
                      numero_kart:
                        type: integer
                        example: 17
                      tempo:
                        type: number
                        format: float
                        example: 58.321
                      posicao:
                        type: integer
                        example: 1
      400:
        description: É necessário ao menos 2 pilotos.
        content:
          application/json:
            schema:
              type: object
              properties:
                erro:
                  type: string
                  example: Cadastre pelo menos 2 pilotos para simular uma corrida.
    """
    return CorridasController.simular_corrida()


@corridas_bp.get("/corridas")
def listar_corridas():
    """
    Lista o histórico de corridas simuladas.
    ---
    summary: Lista o histórico de corridas
    tags:
      - Corridas
    produces:
      - application/json
    responses:
      200:
        description: Histórico de corridas.
        content:
          application/json:
            schema:
              type: object
              properties:
                corridas:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 3
                      data_corrida:
                        type: string
                        example: 2026-03-29T18:35:10
                      resultado:
                        type: array
                        items:
                          type: object
                          properties:
                            piloto_id:
                              type: integer
                              example: 1
                            nome:
                              type: string
                              example: Ayrton Lima
                            numero_kart:
                              type: integer
                              example: 17
                            tempo:
                              type: number
                              format: float
                              example: 58.321
                            posicao:
                              type: integer
                              example: 1
    """
    return CorridasController.listar_corridas()
