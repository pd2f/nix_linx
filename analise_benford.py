import math as m
import pylab as py
import re
from dao import data_linx


def lei_digito_1_benford():
	return [m.log10(1+1/float(i))*100.0 for i in range(1,10)]

def lei_digito_2_benford():
    d2 = []
    vl=0
    for i in range(0,10):
        vl=0
        for j in range(1,10):
            vl+=m.log10(1+1/float(j*10+i))
        d2.append(vl*100)
    return d2


def calcula_digito_1(dados):
   fdigito = [str(dado)[:1] for dado in dados]
   primeiro_d = [fdigito.count(str(i))/float(len(dados))*100 for i in range(1, 10)]
   return primeiro_d

def calcula_digito_2(dados):
    digito = [re.findall(r'\d',str(dado))[1:2][0] for dado in dados]
    return  [digito.count(str(i))/float(len(dados))*100 for i in range(0, 10)]

def pearson_correl(x,y): #fonte - http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
   sizex = len(x)
   sizey = len(y)
   if sizex != sizey: return 0
   if sizey == 0: return 0
   sizen = float(sizex)
   media_x = sum(x)/sizen
   media_y = sum(y)/sizen
   desvio_x = m.sqrt(sum([(a-media_x)*(a-media_x) for a in x])/(sizen-1) )
   desvio_y = m.sqrt(sum([(a-media_y)*(a-media_y) for a in y])/(sizen-1) )
   normx = [(a-media_x)/desvio_x for a in x]
   normy = [(a-media_y)/desvio_y for a in y]
   return sum([normx[i]*normy[i] for i in range(sizex)])/(sizen-1)

def plot_benford_d1(benford, data_ibov, dados_nome):
   xaxis = py.arange(1, 10)
   py.plot(xaxis, benford, linewidth=1.0)
   py.plot(xaxis, data_ibov, linewidth=1.0)
   py.xlabel('Primeiro Digito')
   py.ylabel('Percentual')
   py.title("NIX: %s (Correlacao:  %.2f)" % (dados_nome, pearson_correl(benford, data_ibov)))
   py.legend((dados_nome, "Lei de Benford"))
   return py.show()
  
def plot_benford_d2(benford, data_ibov, dados_nome):
   xaxis = py.arange(0, len(benford))
   py.xscale("linear")
   py.plot(xaxis, benford, linewidth=1.0)
   py.plot(xaxis, data_ibov, linewidth=1.0)
   py.xticks(py.arange(0, len(benford)))
   py.xlabel('Primeiro Digito')
   py.ylabel('Percentual')
   py.title("NIX: %s (Correlacao:  %.2f)" % (dados_nome, pearson_correl(benford, data_ibov)))
   py.legend((dados_nome, "Lei de Benford"))
   return py.show()    

def ajusta(valor):
	v = float(valor.replace(",","."))
	return v


#### Gráficos #####
plot_benford(calcula_digito(data_linx.productTotal), lei_digito_1_benford(), "Dataset - Dados Linx")


cpf_data_linx = data_linx.dropna(subset=['encrypted_buyer_cpf'])
plot_benford_d1(calcula_digito(cpf_data_linx.productTotal), lei_digito_1_benford(), "Primeiros Registros - Dados Linx")
plot_benford_d2(calcula_digito_2(cnpj_data_linx.productTotal), lei_digito_2_benford(), "Pagamentos em Dinheiro - Dados Linx")


cnpj_data_linx = data_linx.dropna(subset=['encrypted_buyer_cnpj']) 
plot_benford_d1(calcula_digito(cnpj_data_linx.productTotal), lei_digito_1_benford(), "Com Registros de CNPJ - Dados Linx")
plot_benford_d2(calcula_digito_2(cnpj_data_linx.productTotal), lei_digito_2_benford(), "Pagamentos em Dinheiro - Dados Linx")

sem_cpf_sem_cnpj_data_linx = data_linx[data_linx.encrypted_buyer_cnpj.isna() & data_linx.encrypted_buyer_cpf.isna()]
plot_benford_d1(calcula_digito(sem_cpf_sem_cnpj_data_linx.productTotal), lei_digito_1_benford(), "Sem Registros de Documentos de Compradores - Dados Linx")
plot_benford_d2(calcula_digito_2(sem_cpf_sem_cnpj_data_linx.productTotal), lei_digito_2_benford(), "Pagamentos em Dinheiro - Dados Linx")

pg_dinheiro = data_linx[data_linx.dinheiro > 0]
plot_benford_d1(calcula_digito(pg_dinheiro.productTotal), lei_digito_1_benford(), "Pagamentos em Dinheiro - Dados Linx")
plot_benford_d2(calcula_digito_2(pg_dinheiro.productTotal), lei_digito_2_benford(), "Pagamentos em Dinheiro - Dados Linx")
