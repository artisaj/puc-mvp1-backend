from flask import Blueprint

from app.controllers.pilotos_controller import PilotosController

pilotos_bp = Blueprint("pilotos", __name__)


@pilotos_bp.post("/pilotos")
def criar_piloto():
    """
    Cadastra um novo piloto.
    ---
    summary: Cadastra um piloto
    tags:
      - Pilotos
    consumes:
      - application/json
    produces:
      - application/json
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              numero_kart:
                type: integer
              equipe:
                type: string
            required:
              - nome
              - numero_kart
    responses:
      201:
        description: Piloto cadastrado com sucesso.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensagem:
                  type: string
                  example: Piloto cadastrado com sucesso.
                id:
                  type: integer
                  example: 1
      400:
        description: Dados inválidos.
        content:
          application/json:
            schema:
              type: object
              properties:
                erro:
                  type: string
                  example: Dados inválidos. Envie 'nome' (texto) e 'numero_kart' (inteiro).
    """
    return PilotosController.criar_piloto()


@pilotos_bp.get("/pilotos")
def listar_pilotos():
    """
    Lista todos os pilotos cadastrados.
    ---
    summary: Lista pilotos
    tags:
      - Pilotos
    produces:
      - application/json
    responses:
      200:
        description: Lista de pilotos.
        content:
          application/json:
            schema:
              type: object
              properties:
                pilotos:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      nome:
                        type: string
                        example: Ayrton Lima
                      numero_kart:
                        type: integer
                        example: 17
                      equipe:
                        type: string
                        nullable: true
                        example: Equipe Azul
                      created_at:
                        type: string
                        example: 2026-03-29 18:00:00
    """
    return PilotosController.listar_pilotos()


@pilotos_bp.get("/pilotos/<int:piloto_id>")
def buscar_piloto(piloto_id):
    """
    Busca um piloto pelo id.
    ---
    summary: Busca um piloto por id
    tags:
      - Pilotos
    parameters:
      - in: path
        name: piloto_id
        schema:
          type: integer
        required: true
    responses:
      200:
        description: Piloto encontrado.
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                nome:
                  type: string
                  example: Ayrton Lima
                numero_kart:
                  type: integer
                  example: 17
                equipe:
                  type: string
                  nullable: true
                  example: Equipe Azul
                created_at:
                  type: string
                  example: 2026-03-29 18:00:00
      404:
        description: Piloto não encontrado.
        content:
          application/json:
            schema:
              type: object
              properties:
                erro:
                  type: string
                  example: Piloto não encontrado.
    """
    return PilotosController.buscar_piloto(piloto_id)


@pilotos_bp.delete("/pilotos/<int:piloto_id>")
def remover_piloto(piloto_id):
    """
    Remove um piloto pelo id.
    ---
    summary: Remove um piloto
    tags:
      - Pilotos
    parameters:
      - in: path
        name: piloto_id
        schema:
          type: integer
        required: true
    responses:
      200:
        description: Piloto removido com sucesso.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensagem:
                  type: string
                  example: Piloto removido com sucesso.
      404:
        description: Piloto não encontrado.
        content:
          application/json:
            schema:
              type: object
              properties:
                erro:
                  type: string
                  example: Piloto não encontrado.
    """
    return PilotosController.remover_piloto(piloto_id)
