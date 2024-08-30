def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
  
    coluna = []

    with open(nome_arquivo, mode='r', encoding='utf8') as arquivo:
        arquivo.readline()

        for linha in arquivo:
            valores = linha.strip().split(',')
            valor = valores[indice_coluna]
           
            if tipo_dado == 'int':
                try:
                    valor_convertido = int(valor)
                except ValueError:
                    print(f"Erro ao converter valor '{valor}' para inteiro.")
                    continue
            elif tipo_dado == 'float':
                try:
                    valor_convertido = float(valor)
                except ValueError:
                    print(f"Erro ao converter valor '{valor}' para float.")
                    continue
            elif tipo_dado == 'str':
                valor_convertido = str(valor)
            else:
                print(f"Tipo de dado '{tipo_dado}' não suportado.")
                return []

            coluna.append(valor_convertido)

    return coluna


valor_venda = extrai_coluna_csv(
 nome_arquivo='carros.csv',
 indice_coluna=1,
 tipo_dado='str'
)
print(valor_venda)

pessoas = extrai_coluna_csv(
 nome_arquivo='./carros.csv',
 indice_coluna=4,
 tipo_dado='int'
)
print(pessoas)