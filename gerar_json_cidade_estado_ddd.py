from typing import List, Dict, Any
from collections import ChainMap
from unicodedata import normalize

import requests
import json


URL_BASE: str = "https://brasilapi.com.br/api/ddd/v1/"

ddds: List[int] = [
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    21,
    22,
    24,
    27,
    28,
    31,
    32,
    33,
    34,
    35,
    37,
    38,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    51,
    53,
    54,
    55,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    71,
    73,
    74,
    75,
    77,
    79,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
]

def formatar_cidade_ddd(dicionario: Dict[str, Any], ddd: int) -> Dict[str, int]:
    estado: str = dicionario.get("state")
    cidades: List[str] = dicionario.get("cities", [])

    resposta: Dict[str, int] = {}
    for cidade in cidades:
        chave: str = normalize("NFKD", f"{estado}-{cidade}").encode("ASCII", "ignore").decode("ASCII")
        resposta.update({chave: ddd})

    return resposta

def processar(lista_de_ddd: List[int]) -> List[Dict[str, int]]:
    lista_de_resposta: List[Dict[str, int]] = []
    for ddd in lista_de_ddd:
        req = requests.get(f"{URL_BASE}{ddd}")
        resposta = formatar_cidade_ddd(req.json(), ddd)
        lista_de_resposta.append(resposta)

    return lista_de_resposta


if __name__ == "__main__":
    lista = processar(lista_de_ddd=ddds)
    dict_final: Dict[str, int] = dict(ChainMap(*lista))
    with open("estado_cidade_por_ddd.json", "w") as outfile:
        outfile.write(json.dumps(dict_final, indent=4, sort_keys=True))
