import PySimpleGUI as sg
import back

sg.theme('DefaultNoMoreNagging')

menu_def = [
    ['Home'],
    ['Cadastros', ['Clientes e Fornecedores::', 'Produtos::', 'Vendedores', 'Relatórios']],
    ['Suprimentos', ['Controle de Estoques', 'Pedidos de Compra'], 'Nota de Entrada', 'Relatórios'],
    ['Vendas'],
    ['Finanças'],
    ['Serviços']
]

def layout_home():
    return [
        [sg.Menu(menu_def)],
        [sg.Text('Um preenchimento de tela abaixo.')],
        [sg.Multiline(size=(60, 20))]
    ]

def layout_clientes_e_produtos():
    return [
        [sg.Menu(menu_def)],
        [sg.Checkbox('Fornecedora GX')],
        [sg.Checkbox('Fornecedor Smart')],
        [sg.Checkbox('Pedro Henrique')],
        [sg.Button('Voltar', key='Home')]
    ]

def layout_produtos():
    def formatar_dados_tabela():
        tabela = back.tabela_produtos.get_table
        if len(tabela) == 0:
            tabela = [['', 'Nenhum produto cadastrado', '', '', '', '', '', '', '', '', '', '', '', '']]
        else:
            for i in tabela:
                for k, v in enumerate(i):
                    if v == '':
                        i[k] = '"Não informado"'
                    elif k == 4:
                        i[k] = f'{v:.2f}'
        return tabela

    headings = 'Id', 'Descrição', 'Código', 'Tipo', 'Preço (R$)', 'Estoque'

    return [
        [sg.Menu(menu_def)],
        [sg.Table(formatar_dados_tabela(), headings, [False, True, True, True, True, True], key='-TABELA_PRODUTOS-'), sg.vtop(sg.Column([
            [sg.Button('Incluir Cadastro', button_color='green', key='-INCLUIR_CADASTRO-')],
            [sg.Button('Visualizar', key='-VISUALIZAR-')],
            [sg.vbottom(sg.Button('Importar Planilha', key='-IMPORTAR_PLANILHA-'))]
        ]))],
        [sg.Button('Voltar', key='Home')]
    ]

def layout_cadastro_produto(dados_produto=None):
    if dados_produto is None:
        dados_produto = ['' for i in range(14)]
        dados_produto[3], dados_produto[6:9], dados_produto[13] = 'Simples', [False for i in range(3)], 'icons/shape.png'

    tab_dados_gerais = [
        [sg.Text('Código (SKU)')], 
        [sg.Input(dados_produto[2], key='-INPUT_CODIGO-')],
        [sg.Text('Tipo')],
        [sg.Combo(['Simples', 'Com variação', 'Com composição'], dados_produto[3], key='-COMBO_TIPO-', size=(43, 1))],
        [sg.Text('Preço')],
        [sg.Input(dados_produto[4], key='-INPUT_PRECO_VENDAS-')],
        [sg.Text('Estoque')],
        [sg.Input(dados_produto[5], key='-INPUT_ESTOQUE-')]
    ]

    tab_tags = [
        [sg.Text('As tags servem para classificar os produtos (Exemplo: Marca, Grupo, Cor, etc...)')],
        [sg.Column([
            [sg.Checkbox('Escritório', dados_produto[6], key='-CHECK1-')],
            [sg.Checkbox('Eletrônico', dados_produto[7], key='-CHECK2-')],
            [sg.Checkbox('Roupas', dados_produto[8], key='-CHECK3-')]
        ])]
    ]

    tab_estoque = [
        [sg.Text('Mínimo')],
        [sg.Input(dados_produto[9], key='-INPUT_MINIMO-')],
        [sg.Text('Máximo')],
        [sg.Input(dados_produto[10], key='-INPUT_MAXIMO-')]
    ]

    tab_tributacao = [
        [sg.Text('Origem')],
        [sg.Combo(['Nacional', 'Estrangeira'], dados_produto[11], key='-COMBO_ORIGEM-', size=(43, 1))],
        [sg.Text('NCM')],
        [sg.Input(dados_produto[12], key='-NCM-')]
    ]

    tab_arquivos_e_imagens = [
        [sg.Text('Aviso', font=('default', 14, ['normal']))],
        [sg.Text('Esse produto ainda não possui imagens.')],
        [sg.Button(image_filename=dados_produto[13], image_size=(200, 200), key='-FOTO_PRODUTO-')],
        [sg.Input(key='-FOTO_ADICIONADA-'), sg.FileBrowse('Adicionar', file_types=(('PNG Files', '.png'), ('GIF Files', '.gif')), key='-IMAGE_FILE_BROWSE-')]
    ]

    return [
        [sg.Text('Descrição*')],
        [sg.Input(dados_produto[1], key='-INPUT_DESCRICAO-')],
        [sg.HorizontalSeparator()],
        [sg.TabGroup([[
            sg.Tab('Dados gerais', tab_dados_gerais),
            sg.Tab('Tags', tab_tags),
            sg.Tab('Estoque', tab_estoque),
            sg.Tab('Tributação', tab_tributacao),
            sg.Tab('Arquivos e imagens', tab_arquivos_e_imagens)
        ]])],
        [sg.Button('SALVAR', button_color='green', key='-SALVAR_PRODUTO-'), sg.Button('CANCELAR', button_color='gray', key='Produtos::')]
    ]

def layout_importar_planilha():
    return [
        [sg.Text('Selecione a planilha que deseja importar')],
        [sg.Input(key='-INPUT_PLANILHA-'), sg.FileBrowse('Buscar', file_types=(('EXCEL Files', '.xlsx'),), key='-SPREADSHEET_FILE_BROWSE-')],
        [sg.Button('SALVAR',button_color='green', key='-SALVAR_PLANILHA-'), sg.Button('CANCELAR', button_color='gray', key='Produtos::')]
    ]