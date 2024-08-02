# lista
nomes = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']

# saida de dados
print(f'Quantidade de nomes: {len(nomes)}.\n')
print('Modo 1:\n')

for nome in nomes:
    print(nome)

print('\nModo 2:\n')

for i in range(len(nomes)):
    print(f'{i + 1}º nome: {nomes[i]}.')