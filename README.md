# Pc-info

## Descrição
Este projeto é uma ferramenta de linha de comando que fornece informações detalhadas sobre o sistema, incluindo o sistema operacional, especificações de hardware, uso de memória, espaço em disco, velocidade de rede e informações da GPU. Utiliza Python e várias bibliotecas para coletar e exibir as informações do sistema de forma estruturada e visualmente atraente.

## Novo Layout
O projeto agora utiliza um layout mais sofisticado e visualmente agradável, dividindo as informações em painéis coloridos e organizados. A saída é apresentada em um formato de dashboard, tornando a leitura das informações mais fácil e intuitiva.

### Exemplo de Saída

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          Informações do Sistema                            │
└────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────┐ ┌─────────────────────────────────────┐
│             Sistema                 │ │               CPU                   │
│ ┌───────────────┬───────────────────┐ │ ┌───────────────┬───────────────────┐
│ │ SO            │ Windows           │ │ │ Cores Físicos │ 4                 │
│ │ Computador    │ DESKTOP-12345     │ │ │ Cores Lógicos │ 8                 │
│ │ Versão SO     │ 10.0.18363        │ │ │ Arquitetura   │ Intel(R) Core(TM) │
│ │ Arquitetura   │ AMD64             │ │ │ Freq. Máxima  │ 3.50 GHz          │
│ │ Processador   │ Intel i5-12345    │ │ │ Freq. Atual   │ 1.20 GHz          │
│ │ Python        │ 3.9.7             │ │ │ Uso da CPU    │ 25.0%             │
│ └───────────────┴───────────────────┘ │ └───────────────┴───────────────────┘
└─────────────────────────────────────┘ └─────────────────────────────────────┘
┌─────────────────────────────────────┐ ┌─────────────────────────────────────┐
│             Memória                 │ │               Disco                 │
│ ┌───────────────┬───────────────────┐ │ ┌───────────────┬───────────────────┐
│ │ Total         │ 16.00 GB          │ │ │ Dispositivo   │ C:                │
│ │ Disponível    │ 12.00 GB          │ │ │ Total         │ 237.00 GB         │
│ │ Em Uso        │ 4.00 GB           │ │ │ Usado         │ 80.00 GB          │
│ │ % de Uso      │ 25.0%             │ │ │ Livre         │ 157.00 GB         │
│ └───────────────┴───────────────────┘ │ │ % de Uso      │ 34.0%             │
└─────────────────────────────────────┘ │ └───────────────┴───────────────────┘
┌─────────────────────────────────────┐ └─────────────────────────────────────┘
│               Rede                  │ ┌─────────────────────────────────────┐
│ ┌───────────────┬───────────────────┐ │                GPU                  │
│ │ Download      │ 50.00 Mbps        │ │ ┌───────────────┬───────────────────┐
│ │ Upload        │ 20.00 Mbps        │ │ │ Nome          │ NVIDIA GTX 12345  │
│ │ Ping          │ 25.00 ms          │ │ │ Memória Total │ 8.00 GB           │
│ │ IP            │ 197.168.0.1       │ │ │ Memória Usada │ 4.00 GB           │
│ │ ISP           │ MeuISP            │ │ │ % de Uso      │ 60.00%            │
│ └───────────────┴───────────────────┘ │ └───────────────┴───────────────────┘
└─────────────────────────────────────┘ └─────────────────────────────────────┘
```

## Dependências
Para executar este projeto, você precisa ter as seguintes dependências instaladas:

- platform
- psutil
- rich
- speedtest-cli
- GPUtil (opcional, para informações da GPU)

Você pode instalar essas dependências usando o pip:

```
pip install rich psutil speedtest-cli gputil
```

## Uso
Para utilizar esta ferramenta, execute o script Pc-info.py utilizando o Python:

```
python Pc-info.py
```

O script exibirá as informações do sistema no terminal/console em um layout organizado e visualmente atraente.

## Recursos
- Layout de dashboard dividido em seções coloridas
- Informações detalhadas sobre sistema, CPU, memória, disco, rede e GPU
- Uso de cores para melhor legibilidade
- Apresentação organizada e intuitiva das informações

## Licença
Este projeto está licenciado sob a Licença MIT.
