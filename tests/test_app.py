import unittest
# Em test_app.py
from app.models import Animal, Recinto, Zoologico

class TestZoologico(unittest.TestCase):

    def test_criacao_animal(self):
        animal = Animal("Simba", "Leão", 5)
        self.assertEqual(animal.nome, "Simba")
        self.assertEqual(animal.especie, "Leão")
        self.assertEqual(animal.nivel_felicidade, 5)

    def test_alimentar_animal(self):
        #Animal será criado sem felicidade total para vermos ele se alimentando 
        animal = Animal("Simba", "Leão", 4)
        animal.alimentar()
        self.assertEqual(animal.nivel_felicidade, 5)

    def test_alimentar_animal_feliz(self):
        # teste com animal já feliz, não deverá alterar sua felicidade
        animal = Animal("Simba", "Leão", 5)
        animal.alimentar()
        self.assertEqual(animal.nivel_felicidade, 5)

    def test_criacao_recinto(self):
        recinto = Recinto("Recinto 1", 5)
        self.assertEqual(recinto.nome, "Recinto 1")
        self.assertEqual(recinto.cuidado, 5)

    def test_adicionar_animal_recinto(self):
        recinto = Recinto("Recinto 1", 5)
        animal = Animal("Trovão", "Cachorro", 5)
        recinto.adicionar_animal(animal)
        self.assertIn(animal, recinto.animais)

    def test_alterar_cuidado_cuidar(self):
        # Recinto criado sem cuidado total para que ele possa ser cuidado
        recinto = Recinto("Recinto 1", 4)
        recinto.alterar_cuidado('cuidar')
        self.assertEqual(recinto.cuidado, 5)

    def test_alterar_cuidado_descuidar(self):
        # Recinto criado sem cuidado total para que ele possa ser descuidado
        recinto = Recinto("Recinto 1", 4)
        recinto.alterar_cuidado('descuidar')
        self.assertEqual(recinto.cuidado, 3)

    def test_alterar_cuidado_max_cuidado(self):
        # Recinto criado sem cuidado total para que ele possa ser cuidado
        recinto = Recinto("Recinto 1", 5)
        recinto.alterar_cuidado('cuidar')
        self.assertEqual(recinto.cuidado, 5)

    def test_alterar_cuidado_min_cuidado(self):
        # Recinto criado sem cuidado total para que ele possa ser cuidado
        recinto = Recinto("Recinto 1", 0)
        recinto.alterar_cuidado('descuidar')
        self.assertEqual(recinto.cuidado, 0)

    def test_adicionar_recinto(self):
        zoologico = Zoologico()
        recinto = Recinto('Recinto 0', 5)
        zoologico.adicionar_recinto(recinto)
        self.assertIn(recinto, zoologico.recintos)
    # Mais testes seriam adicionados aqui...

    def test_receber_visitantes(self):
        zoologico = Zoologico()
        recinto = Recinto('Recinto 0', 5)
        zoologico.adicionar_recinto(recinto)
        animal = Animal("Thor", "Gato", 5)
        recinto.adicionar_animal(animal)
        zoologico.receber_visitantes()

        #Criamos um zoologico com um recinto de cuidado 5 e um animal de felicidade 5. Dessa forma, é esperado que existam 25 visitantes e o caixa então seja de 25.30 = 750
        self.assertEqual(zoologico.caixa, 750)


if __name__ == '__main__':
    unittest.main()
