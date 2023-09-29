FROM codercom/code-server:latest

RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends wget python3-venv python3-pip gcc g++ nodejs npm unzip ripgrep fd-find ncdu && sudo rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz 
RUN sudo npm install -g tree-sitter-cli
RUN pip3 install pynvim

RUN sudo tar xzvf nvim-linux64.tar.gz -C /usr && rm nvim-linux64.tar.gz
RUN sudo ln -s /usr/nvim-linux64/bin/nvim /usr/local/bin/nvim
