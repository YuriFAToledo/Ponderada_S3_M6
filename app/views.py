from flask import Flask, jsonify, request
from app.models import Animal, Recinto, Zoologico


app = Flask(__name__)
zoologico = Zoologico()

@app.route('/animais', methods=['POST'])
def criar_animal():
    data = request.get_json()
    animal = Animal(data['nome'], data['especie'])

    # por padrão o animal será adicionado no primeiro recinto
    zoologico.recintos[0].adicionar_animal(animal)
    
    return jsonify({'status': 'sucesso'}), 201

@app.route('/animais/alimentar', methods=['POST'])
def alimentar():
    data = request.get_json()
    nome = data['nome']
    especie = data['especie']

    if not nome or not especie:
        return jsonify({'error': 'Nome e espécie são necessários para alimentar um animal.'}), 400

    animal_encontrado = None
    for recinto in zoologico.recintos:
        for animal in recinto.animais:
            if animal.nome == nome and animal.especie == especie:
                animal_encontrado = animal
                break
        if animal_encontrado:  # Se o animal foi encontrado, não precisa continuar procurando
            break

    if not animal_encontrado:
        return jsonify({'error': 'Animal não encontrado.'}), 404

    # Alimentar o animal encontrado
    animal_encontrado.alimentar()
    return jsonify({'status': 'sucesso', 'mensagem': f'{nome} foi alimentado com sucesso!'}), 200

@app.route('/recintos', methods=['POST'])
def criar_recinto():
    data = request.get_json()
    nome = data['nome']
    recinto = Recinto(nome)
    zoologico.adicionar_recinto(recinto)

@app.route('/recintos/adicionar_animal', methods=['POST'])
def adicionar_animal():
    data = request.get_json()
    animalNome = data['animalNome'] 
    animalEspecie = data['animalEspecie'] 
    recintoNome = data['recintoNome']

    if not animalNome or not animalEspecie:
        return jsonify({'error': 'Nome e espécie são necessários para alimentar um animal.'}), 400

    recinto_encontrado = None
    animal_encontrado = None
    for recinto in zoologico.recintos:
        if recinto.nome == recintoNome:
            recinto_encontrado = recinto
        for animal in recinto.animais:
            if animal.nome == animalNome and animal.especie == animalEspecie:
                animal_encontrado = animal
                break
        if animal_encontrado:  # Se o animal foi encontrado, não precisa continuar procurando
            break

    if not animal_encontrado:
        return jsonify({'error': 'Animal não encontrado.'}), 404

    recinto_encontrado.adicionar_animal(animal_encontrado)
    print(f"Animal {animal_encontrado.nome} adicionado com sucesso ao recinto {recinto_encontrado.nome}")

@app.route('/recintos/alterar_cuidado', methods=['POST'])
def alterar_cuidado():
    data = request.get_json()
    acao = data['acao']

    recinto_encontrado = None

    for recinto in zoologico.recintos:
        if recinto.nome == recintoNome:
            recinto_encontrado = recinto
            break

    if(recinto_encontrado):
        recinto_encontrado.alterar_cuidado(acao)
    else: 
        print("Recinto não encontrado")

@app.route('/zoo/receber_visitante', methods=['POST'])
def receber_visitante():
    zoologico.receber_visitantes()

if __name__ == '__main__':
    app.run(debug=True)
