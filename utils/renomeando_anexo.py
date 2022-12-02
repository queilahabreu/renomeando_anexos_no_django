from django.utils.deconstruct import deconstructible

@deconstructible
class RenomeandoAnexo(object):

    def __init__(self, nome_arquivo, nome_acao, tipo_extensao):
        self.nome_arquivo = nome_arquivo 
        self.nome_acao = nome_acao
        self.tipo_extensao = tipo_extensao

    def __call__(self, instance, filename):
        path ='uploads/'+self.nome_acao+'/'+str(instance.id)
        filename = self.nome_arquivo
        return f'{path}/{filename}{self.tipo_extensao}'
