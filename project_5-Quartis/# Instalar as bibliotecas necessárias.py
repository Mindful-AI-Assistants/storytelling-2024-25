# Instalar as bibliotecas necessárias
!pip install pandas numpy matplotlib contourpy cycler fonttools kiwisolver packaging pillow pyparsing python-dateutil

# Importar as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Verificar se as bibliotecas foram instaladas corretamente
print(f"Pandas versão: {pd.__version__}")
print(f"Numpy versão: {np.__version__}")
print(f"Matplotlib versão: {plt.__version__}")