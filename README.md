# 📂 Organizador e Buscador de Arquivos em Python

## 🧠 Descrição
Este projeto é um script em Python que organiza automaticamente arquivos de uma pasta com base na extensão e permite buscar arquivos por data (dia, mês, ano ou data completa).

---

## ⚙️ Funcionalidades

- 📁 Organização automática de arquivos por tipo
- 🗂️ Criação de pastas automaticamente
- 🔄 Movimentação de arquivos para suas respectivas pastas
- 🔍 Busca opcional por data:
  - Por dia
  - Por mês
  - Por ano
  - Data completa
- 🧭 Menu interativo para escolha do tipo de busca

---

## 🛠️ Tecnologias utilizadas

- Python
- Biblioteca `os`
- Biblioteca `shutil`
- Biblioteca `datetime`
- Biblioteca `logging`

---

## 📁 Estrutura do projeto
📦 projeto
┣ 📜 main.py
┣ 📜 colocar_caminho.py
┣ 📜 dicionario.py
┣ 📜 categorizacao_de_arquivos.py
┣ 📜 cria_move.py
┣ 📜 busca_datetime.py
┗ 📜 README.md
---

## 🚀 Como usar

1. Execute o arquivo principal:

```bash
python main.py
Insira o caminho da pasta que deseja organizar
O programa irá:
Categorizar os arquivos
Criar pastas automaticamente
Mover os arquivos
Em seguida, você poderá:
Escolher uma pasta
Buscar arquivos por data (opcional)

💡 Exemplos de uso
Organizar a pasta Downloads
Buscar imagens de um dia específico
Encontrar documentos de um determinado mês
Filtrar arquivos por ano
📌 Extensões suportadas

O sistema organiza arquivos com base em extensões como:

🎵 Áudio: mp3, wav, flac...
🎬 Vídeo: mp4, mkv, avi...
🖼️ Imagens: jpg, png, avif...
📄 Documentos: pdf, docx, xlsx...
📦 Compactados: zip, rar...
💻 Scripts: py, js, html...
⚙️ Executáveis: exe, msi...
🎮 Demos: dem

(As extensões podem ser facilmente modificadas no arquivo dicionario.py)

🔮 Melhorias futuras
📦 Categoria "outros" para arquivos não identificados
🤖 Integração com IA para busca por conteúdo de imagem
🌐 Transformar o projeto em uma API (Flask ou FastAPI)
🖥️ Interface gráfica
👨‍💻 Autor

Desenvolvido como projeto de estudo em Python focado em:

Manipulação de arquivos
Estrutura de projetos
Boas práticas de programação

