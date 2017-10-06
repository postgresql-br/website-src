### 0) Instalando dependências

    sudo apt install git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils


### 1) Instalando pyenv

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc


### 2) Instalando Python 3.5.2

    pyenv install 3.5.2


#### Dependencias

```bash 
pip3 install -r requirements.txt
```

### 5) Construção

    make html

O conteúdo estático estará na pasta `output`.


### 6) Desenvolvimento

    make devserver

Construirá o conteúdo estático e iniciará um servidor web local na porta 8000. Para parar o servidor:

    make stopserver


### 7) Colocar conteúdo estático no postgresql-br.github.io

Após compilar com `make html`, o conteúdo estático estará na pasta `output`. É necessário também clonar o repositório http://github.com/postgresql-br/postgresql-br.github.io, e colocá-lo na mesma pasta em que o repositório atual está.

    mv output/* ../postgresql-br.github.io/
    rmdir output


### 8) Orientações Gerais

Artigos são escritos em formato MD e ficam na pasta `content`.

Páginas também são escritas em formato MD e ficam na pasta `content/pages`.

Imagens ficam na pasta `content/images`.

O arquivo `content/css/custom.css` contém nossas correções no tema adotado. Corrige o layout de tabelas e também faz o header funcionar em smartphones.
