from django.utils.deconstruct import deconstructible

@deconstructible
class RenomeandoAnexo(object):

    def __init__(self, nome_arquivo, nome_acao):
        self.nome_arquivo = nome_arquivo 
        self.nome_acao = nome_acao

    def __call__(self, instance, filename):
        path ='uploads/'+self.nome_acao+'/'+str(instance.id)
        #extraindo a extensão do arquivo
        separator = filename.split('.')
        filename = self.nome_arquivo
        return f'{path}/{filename}.{separator[1]}'

path_and_rename = RenomeandoAnexo('teste','teste')
