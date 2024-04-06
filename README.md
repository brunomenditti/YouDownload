# YouTube Downloader

Este projeto é um aplicativo simples de interface gráfica (GUI) desenvolvido em Python que permite aos usuários baixar vídeos do YouTube especificando o link do vídeo. Os vídeos são baixados na melhor resolução disponível e salvos em um diretório `downloads` no diretório do aplicativo.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em seu sistema. Este projeto foi testado com Python 3.8+. Você também precisará das seguintes bibliotecas:

- tkinter
- customtkinter
- pytube

Você pode instalar todas as dependências necessárias executando:

```bash
pip install tkinter customtkinter pytube
```

## Executando o Projeto

Para executar o projeto diretamente usando Python, navegue até o diretório do projeto em seu terminal e execute:

```bash
python main.py
```

## Convertendo o Código Python em um Executável (.exe)

Para distribuir este aplicativo como um executável standalone no Windows, você pode usar PyInstaller. Siga estas etapas para converter seu script Python em um arquivo .exe:

1. **Instale o PyInstaller** (se ainda não estiver instalado):

```bash
pip install pyinstaller
```

2. **Navegue até o diretório do projeto** onde o arquivo `main.py` está localizado.

3. **Execute o PyInstaller** com as opções desejadas. Por exemplo, para criar um único arquivo executável sem console:

```bash
pyinstaller --onefile --windowed --icon=seu_icone.ico main.py
```

Substitua `seu_icone.ico` pelo caminho do seu arquivo de ícone, se desejar adicionar um ícone personalizado ao executável.

4. **Localize o Executável**: Após a conclusão do processo, o PyInstaller criará uma pasta `dist` no diretório do projeto. Seu arquivo .exe estará dentro dessa pasta.

## Estrutura do Projeto

O projeto contém os seguintes arquivos principais:

- `main.py`: O script Python principal que executa o aplicativo de downloader do YouTube.

- `README.md`: Este arquivo, que fornece informações sobre o projeto e instruções para executá-lo e convertê-lo em um executável.

## Contribuindo

Contribuições para o projeto são bem-vindas! Sinta-se à vontade para forkar o repositório, fazer suas alterações e abrir um pull request.
