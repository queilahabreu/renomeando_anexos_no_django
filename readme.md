<h1 align="center">Renomeando Anexos (FileField/ImageField) - Django</h1>

<p align="center">Renomear arquivos de tipo FileField e ImageField antes de salvar no sistema.</p>

![Badge](https://img.shields.io/badge/Django-4.0.4-brightgreen?style=for-the-badge)


=================
<!--ts-->
   * [Sobre os Parâmetros](#Sobre-os-parametros)
        * ```
            ...
                atributo = models.FileField(upload_to=RenomeandoAnexo('nome_arquivo','nome_acao'))
            ...
            ```
        * nome_arquivo
            * Nome que você deseja renomear o arquivo
        * nome_acao
            * Nome especifico sobre o tipo de cadastro
   * [Observação](#Observacao)
        * Para o instance.id funcionar é preciso que modifique o ID na model, coloque como campo UUIDField
        * ```
            id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, verbose_name="Id")
            ```
   * [Exemplo](#Exemplo)
        * Cadastro de animais, dentro do models ficaria:
        * ```
            from utils.renomeando_anexo import *
            ...
            class Animal(models.Model):
            ...
                carteira_vacinacao_anexo = models.FileField(upload_to=RenomeandoAnexo('carteira_vacinacao','cadastro_animal'), blank=True, null = True,verbose_name="Carteira de Vacinação")
            ...
            ```
        * Caminho final do arquivo: media/uploads/cadastro_animal/099d5f3f-3795-4cae-8b18-d40dfd98b1b7/carteira_vacinacao.pdf
   * [Referências](#Referencias)
        * https://docs.djangoproject.com/en/4.0/ref/models/fields/
        * https://docs.djangoproject.com/en/4.1/topics/migrations/#adding-a-deconstruct-method
        * https://stackoverflow.com/questions/59871248/django-cannot-make-makemigrations
        * https://acervolima.com/__call__-em-python/
        * https://stackoverflow.com/questions/2680391/how-to-change-the-file-name-of-an-uploaded-file-in-django
        * https://stackoverflow.com/questions/4110581/change-filename-before-save-file-in-django
<!--te-->
