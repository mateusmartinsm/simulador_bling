from views import *
from back import Produto
import pandas as pd

layout_key_list = {
    'Home': layout_home,
    'Clientes e Fornecedores::': layout_clientes_e_produtos,
    'Produtos::': layout_produtos,
    '-INCLUIR_CADASTRO-': layout_cadastro_produto,
    '-IMPORTAR_PLANILHA-': layout_importar_planilha
}

input_key_list = ['-INPUT_DESCRICAO-', '-INPUT_CODIGO-', '-COMBO_TIPO-', '-INPUT_PRECO_VENDAS-', '-INPUT_ESTOQUE-', '-CHECK1-', '-CHECK2-', '-CHECK3-', '-INPUT_MINIMO-', '-INPUT_MAXIMO-', '-COMBO_ORIGEM-', '-NCM-']

produto = Produto()
window = sg.Window('Bling Simulator', layout_home())

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in layout_key_list:
        window.close()
        window = sg.Window(title='Bling Simulator', layout=layout_key_list[event]())
    elif event == '-VISUALIZAR-':
        try:
            dados_produto = window['-TABELA_PRODUTOS-'].get()[values['-TABELA_PRODUTOS-'][0]]
        except IndexError:
            sg.popup('Selecione um item da lista')
        else:
            window.close()
            window = sg.Window(title='Bling Simulator', layout=layout_cadastro_produto(dados_produto))
    elif event == '-FOTO_PRODUTO-':
        window['-IMAGE_FILE_BROWSE-'].click()
        path_imagem = window['-FOTO_ADICIONADA-'].get()
        window['-FOTO_PRODUTO-'].update(image_filename=path_imagem)
    elif event == '-SALVAR_PRODUTO-':
        informacoes_novo_produto = [window[i].get() for i in input_key_list]
        informacoes_novo_produto.append(path_imagem)
        produto.cadastrar_produto(informacoes_novo_produto)
        sg.popup('Produto cadastrado com sucesso!')
        window.close()
        window = sg.Window(title='Bling Simulator', layout=layout_produtos())
    if event == '-SALVAR_PLANILHA-':
        path_planilha = window['-INPUT_PLANILHA-'].get()
        df = pd.read_excel(path_planilha)
        planilha = [list(df.loc[i]) for i in range(len(df))]
        for c in planilha:
            for i, v in enumerate(c):
                if i in (1, 4, 8, 9):
                    c[i] = int(v)
                elif i in (3, 11):
                    c[i] = float(v)
                elif i in (5, 6, 7):
                    c[i] = eval(str(v))
            produto.cadastrar_produto(c)
        sg.popup('Planilha importada com sucesso')
        window.close()
        window = sg.Window(title='Bling Simulator', layout=layout_produtos())