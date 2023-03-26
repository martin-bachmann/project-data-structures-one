def exists_word(word, instance):
    resposta = []

    for index in range(0, len(instance)):
        arquivo = instance.search(index)
        dados_do_arquivo = {
            "palavra": word,
            "arquivo": arquivo["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index_2 in range(0, arquivo["qtd_linhas"]):
            if word.lower() in arquivo["linhas_do_arquivo"][index_2].lower():
                dados_do_arquivo["ocorrencias"].append({"linha": index_2 + 1})

        if len(dados_do_arquivo["ocorrencias"]) > 0:
            resposta.append(dados_do_arquivo)

    return resposta


def search_by_word(word, instance):
    resposta = []

    for index in range(0, len(instance)):
        arquivo = instance.search(index)
        dados_do_arquivo = {
            "palavra": word,
            "arquivo": arquivo["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index_2 in range(0, arquivo["qtd_linhas"]):
            if word.lower() in arquivo["linhas_do_arquivo"][index_2].lower():
                dados_do_arquivo["ocorrencias"].append(
                    {
                        "linha": index_2 + 1,
                        "conteudo": arquivo["linhas_do_arquivo"][index_2],
                    }
                )

        if len(dados_do_arquivo["ocorrencias"]) > 0:
            resposta.append(dados_do_arquivo)

    return resposta
