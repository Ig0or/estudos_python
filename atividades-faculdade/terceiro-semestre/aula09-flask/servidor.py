from flask import Flask, jsonify, request

app = Flask(__name__)

db_faculdade = {
    "alunos": [
        {"id": 12, "nome": "José"},
    ],
    "professores": [
        {"id": 27, "nome": "Augusto"},
    ],
}

# Teste 0 - Retorna lista alunos
@app.route("/alunos")
def aluno():
    return jsonify(db_faculdade["alunos"])


# Teste 1 - Adiciona aluno
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    dict_aluno = request.json
    db_faculdade["alunos"].append(dict_aluno)
    return jsonify(db_faculdade["alunos"])


# Teste 2 - Retorna aluno por ID
@app.route("/alunos/<int:id_aluno>")
def procura_aluno(id_aluno):
    for aluno in db_faculdade["alunos"]:
        if aluno["id"] == id_aluno:
            return jsonify(aluno)


# Teste 3 - Reseta
@app.route("/reseta", methods=["POST"])
def reseta():
    db_faculdade["alunos"] = []
    db_faculdade["professores"] = []
    return jsonify(db_faculdade)


# Teste 4 - Remove
@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def apaga_aluno(id_aluno):
    for aluno in db_faculdade["alunos"]:
        if aluno["id"] == id_aluno:
            db_faculdade["alunos"].remove(aluno)
    return jsonify(db_faculdade["alunos"])


# Teste 5 - Altera nome
@app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def alterar_nome(id_aluno):
    novo_nome = request.json
    for aluno in db_faculdade["alunos"]:
        if aluno["id"] == id_aluno:
            aluno["nome"] = novo_nome["nome"]
    return jsonify(db_faculdade["alunos"])


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
