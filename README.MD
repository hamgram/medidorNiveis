# Monitoramento de Nível de Reservatório 💧

## Sobre
Este projeto foi desenvolvido como um exercício prático para aplicar conceitos fundamentais de programação. O objetivo é simular um sistema de monitoramento que automatiza a leitura de dados (neste caso, simulada via sorteio) e entrega uma resposta visual clara ao usuário, unindo lógica de decisão e interação via terminal.

---

## 🚀 Funcionalidades

- **Simulação Aleatória**: Gera um nível de água de 0 a 4 sempre que o script é executado através da biblioteca `random`.
- **Categorização de Níveis**: Trabalha com cinco estados distintos:
  - Muito baixo (crítico)
  - Baixo
  - Médio
  - Alto
  - Muito Alto (alerta)
- **Feedback Visual**: Utiliza a biblioteca `colorama` para colorir a saída no terminal, facilitando a interpretação rápida do status.

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem base do projeto.
- **Colorama**: Biblioteca para estilização de cores e estilos no console.

## 📋 Pré-requisitos

Para que as cores funcionem corretamente no seu terminal, instale a biblioteca necessária:

```bash
pip install colorama
```

## 🔧 Como Executar

1. Salve o código em um arquivo chamado `main.py` (ou o nome de sua preferência).
2. No terminal, navegue até a pasta do arquivo.
3. Execute o comando:
   ```bash
   python main.py
   ```

## 📖 Estrutura do Código

O script segue o fluxo padrão de processamento de dados:

1.  **Entrada**: Uma variável define o nível de água aleatoriamente usando `random.randint(0,4)`.
2.  **Processamento**: A função `selecionarCor` utiliza a estrutura `match-case` para definir qual cor do `colorama` será aplicada com base no índice gerado.
3.  **Saída**: Exibe a mensagem final no terminal com o nível em caixa alta e aplica o `Style.RESET_ALL` para evitar que as cores afetem os comandos seguintes do sistema.

---
Desenvolvido para fins educacionais de lógica de programação e uso de bibliotecas python.