import pytest
from common import CommonTests
from utils import imc_classfication

imc_classfication_test_data = [
    (50, 1.75, 'Abaixo do peso'),
    (70, 1.75, 'Peso normal'),
    (90, 1.75, 'Sobrepeso'),
    (104, 1.84, 'Obesidade grau I'),
    (120, 1.75, 'Obesidade grau II'),
    (130, 1.75, 'Obesidade grau III')
]

class TestUtils(CommonTests):
    @pytest.mark.parametrize(
        'weight,height,expected_response',
        imc_classfication_test_data
    )
    def test_imc_classification(self, weight, height, expected_response):
        print(f'weight: {weight}, height: {height}, response: {expected_response}')
        classification = imc_classfication(weight, height)
        print(f'classification: {classification}')
        self.assertEqual(classification, expected_response)
