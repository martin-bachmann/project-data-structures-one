from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(0, len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    linhas = txt_importer(path_file)

    instance.enqueue(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(linhas),
            "linhas_do_arquivo": linhas,
        }
    )

    print(instance)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
