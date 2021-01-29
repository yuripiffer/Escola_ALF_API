#
# ESCOLA_ALF_CODIGO_LOGICA

PROVA = {}

ALUNO = {}

## -----------  CÓDIGOS AUXILIARES  -----------
# Checa o tamanho da string id passada;
def id_valido (input_texto):
  if len(str(input_texto)) == 4:
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Transforma o id em maiúsculo;
def id_upper(input_texto):
  id_val = str(input_texto)[0:4].upper()
  return id_val
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Transforma textos de nome e título maiúsculos e com 50 caracteres
def texto_upper(input_texto):
  texto = str(input_texto)[0:50].upper()
  return texto
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retonra inteiro maior que zero ou False
def int_positivo(numero):
  if int(numero)>0:
    return int(numero)
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Checa se prova existe
def prova_existe(idPROVA):
  if idPROVA in PROVA.keys():
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria os values de um idPROVA
def criar_lists_info_quest(idPROVA):
  n = PROVA[str(idPROVA)]['n_questões']
  x = PROVA[str(idPROVA)]['info_questões']
  x.append(['Nº Questão', 'Resposta', 'Peso'])
  for i in range(0, n+1):
    x.append([])
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria os values de uma idPROVA cadastrada para um idALUNO
def criar_lists_info_quest_ALUNOS(idALUNO, idPROVA):
  n = PROVA[str(idPROVA)]['n_questões']
  x = ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)]
  lista = []
  lista.append(int(n))
  for i in range (1, n+1):
    lista.append([i, ''])
  ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)] = lista.copy()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Avalia se a questão escolhida está dentro do número de questões da idPROVA
def q_menor_totalq(idPROVA, q):
  if q<= PROVA[str(idPROVA)]['n_questões']:
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retorna uma lista com número de questões, repostas e boleano se a prova está completa
# ou retonra lista vazia
def cond_prova(idPROVA):
  x = PROVA[str(idPROVA)]['info_questões']
  n = PROVA[str(idPROVA)]['n_questões']
  if x == []: #se é uma lista vazia
    return [0] #returna uma lista com 0
  else:
    resposta = ''
    completo = True
    lista = []
    lista.append(int(n)) #número de questões
    for i in range(1,n+1): #resposta das questões ou 0
      if x[i][1] in ['A','B','C','D','E']:
        resposta = str(x[i][1])
      else:
        resposta = 0
        completo = False #se qualquer resposta não estiver cadastrada, completo se torna falso
      lista.append(resposta)
    lista.append(completo)
    
    # exemplo --> []
    # exemplo --> [5, 'A', 'C', 'D' , 0, 'D', False] ou 
    # exemplo --> [3, 'C', 'A', 'A', True]
    return lista
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Avalia se a alternativa passada é ['A','B','C','D','E'] ou retonra False
def func_alternativa(texto):
  alternativa = str(texto)[0:1].upper() 
  if alternativa in ['A','B','C','D','E']:
    return alternativa
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Avalia a existência do idALUNO
def aluno_existe(idALUNO):
  if idALUNO in ALUNO.keys():
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Avalia se o número de alunos cadastrados é menor que 100
def aluno_menor100 ():
  if len(ALUNO)<100:
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Avalia se uma idPROVA está cadastrada para um idALUNO
def aluno_prova_existe(idALUNO, idPROVA):
  if idPROVA in ALUNO[str(idALUNO)]['provas_aluno']:
    return True
  else:
    return False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retorna uma lista com número de questões, repostas e boleano se a prova está completa
# ou retonra lista vazia
def cond_aluno_prova(idALUNO, idPROVA):
  x= ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)]
  if x == []: #ainda não recebeu as respostas da prova
    return [0]  
  else:
    n = x[0] #número de questões
    resposta = ''
    completo = True
    lista = []
    lista.append(int(n)) #número de questões
    for i in range(1,n+1): #resposta das questões ou 0
      if x[i][1] in ['A','B','C','D','E']:
        resposta = str(x[i][1])
      else:
        resposta = 0
        completo = False #se qualquer resposta não estiver cadastrada, completo se torna False
      lista.append(resposta)
    lista.append(completo)
    
    # exemplo --> [5, 'A', 'C', 'D' , 0, 'D', False]
    # exemplo --> [3, 'C', 'A', 'A', True]
    return lista
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retorna lista com idPROVA de provas completas
def provas_completas():
  todas_provas = PROVA.keys()
  provas_completas = []
  for p in todas_provas:
    lista = []
    lista = cond_prova(p) #cond_prova devolve [] ou [nº quest, 'B', 'E', 'A', True]
    if lista[-1] == True:
      provas_completas.append(str(p))
  return provas_completas
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retorna lista com idPROVA de provas completas para um determinado aluno
def aluno_provas_completas(idALUNO): 
  todas_provas_aluno = ALUNO[str(idALUNO)]['provas_aluno'].keys()
  aluno_provas_completas = [] # se não tiver aluno, retorna vazia
  for p in todas_provas_aluno:
    lista = cond_aluno_prova(idALUNO, p)
    if lista[-1] == True:
      aluno_provas_completas.append(str(p))
  return aluno_provas_completas
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Retonra uma lista com o idALUNO e idPROVA das provas com tudo pronto para computar nota para o aluno em questão
def provas_computaveis_aluno (idALUNO):
  provas_completas_dictPROVA = provas_completas()
  aluno_provas_completas_dictALUNO = aluno_provas_completas(idALUNO)
  if aluno_provas_completas_dictALUNO == []:
    return []
  else:
    provas_computaveis_aluno = []
    provas_computaveis_aluno.append(str(idALUNO))
    for p_aluno in aluno_provas_completas_dictALUNO:
      if p_aluno in provas_completas_dictPROVA:
        provas_computaveis_aluno.append(str(p_aluno)) 
    return provas_computaveis_aluno
    #ex: ['PIFF', 'MATE', 'FISI', 'HIS1'] --> aluno, prova, prova, prova
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Cálculo de nota do idALUNO na idPROVA 
def calcula_nota(idALUNO, idPROVA):
  n = PROVA[str(idPROVA)]['n_questões']
  xprova = PROVA[str(idPROVA)]['info_questões']
  xaluno = ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)]
  pontos_aluno = 0
  pontos_maximos = 0
  for i in range(1, n+1):
    pontos_maximos += xprova[i][2]
    if xaluno[i][1] == xprova[i][1]:
      pontos_aluno += xprova[i][2]
  try:
    nota = float((pontos_aluno/pontos_maximos)*10)
  except:
    nota = 0
  return nota
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


## -----------  CÓDIGOS PARA GET, POST, PUT, DELETE  -----------

#TIPO POST PROVA --------------------------------------------------------------------------
def criar_prova(idPROVA, titulo, n_questões):
  if not id_valido(idPROVA):
    return 'O valor inserido para o id tem mais ou menos que 4 caracteres. Tente novamente.'
  idPROVA = id_upper(idPROVA) #Transforma o idPROVA em uppercase
  if prova_existe(idPROVA):
    return 'A prova {} já consta no sistema.'.format(idPROVA)
  n_questões = int_positivo(n_questões) #retonra o int(n_questões) ou False para valor menor que 1
  if not n_questões:
      return 'Ops! O valor inserido para o número de questões é menor que 1.'
  titulo = texto_upper(titulo) #Transforma a string de titulo em uppercase e limita a 50 caracteres 
  PROVA[str(idPROVA)] =  {'titulo': str(titulo), 'n_questões': int(n_questões), 'info_questões':[]}
  return PROVA

#TIPO GET PROVA ------------------------------------------------------------------------------
def info_prova(idPROVA):
  if not id_valido(idPROVA):
    return 'O valor inserido para o id tem mais ou menos que 4 caracteres. Tente novamente.'
  idPROVA = id_upper(idPROVA) #Transforma o idPROVA em uppercase
  if not prova_existe(idPROVA):
    return 'A prova {} ainda não consta no sistema.'.format(idPROVA)
  x = PROVA[str(idPROVA)]
  info_prova = []
  if x['info_questões'] == []:
    info_prova = 'As questões ainda não foram cadastradas.'
  else:
    info_prova.append(['idPROVA: {}, Título da prova: {}, Número de questões: {}'.format(idPROVA, x['título'], x['n_questões'])])
    for i in range(1, x['n_questões']+1):
      info_prova.append('Questão:'+ str(x['info_questões'][i][0]) +' --> Resposta: ' + str(x['info_questões'][i][1]) +', peso: ' + str(x['info_questões'][i][2]))
  return info_prova

#TIPO GET PROVAS -----------------------------------------------------------------------------
def info_total_provas():
  texto = []
  texto.append('PROVAS CADASTRADAS:')
  for k,v in PROVA.items():
    texto.append('Prova {}, {}'.format(k, v['título']))
  return texto

#TIPO POST QUESTÃO PROVA----------------------------------------------------------------------
def preencher_quest_prova(idPROVA, q, resposta, peso):
  #Condições para preencher a questão
  if not id_valido(idPROVA):
    return 'O valor inserido para o id tem mais ou menos que 4 caracteres. Tente novamente.'
  idPROVA = id_upper(idPROVA) #Transforma o idPROVA em uppercase
  if not prova_existe(idPROVA):
    return 'A prova {} não consta no sistema.'.format(idPROVA)
  if not int_positivo(q):
    return 'Ops! O valor inserido para o número da questão é menor que 1.'
  if not q_menor_totalq(idPROVA, q):
    return 'O número de questão escolhido é diferente do número de questões que a prova tem.'   
  if not int_positivo(peso):
    return 'Ops! O valor inserido para o peso da questão é menor que 1.'
  if not func_alternativa(resposta):
    return 'Ops! O valor inserido para a resposta da pergunta não é A, B, C, D ou E.'
  else:
    alternativa =  func_alternativa(resposta) 

  #Se os campos de questões ainda não foi criado:
  if PROVA[str(idPROVA)]['info_questões'] == []:
    criar_lists_info_quest(idPROVA)
  # Preenchimento da questão
  PROVA[str(idPROVA)]['info_questões'][q] = [int(q), str(alternativa), int(peso)]
  return PROVA[str(idPROVA)]

# TIPO POST ALUNO ----------------------------------------------------------------------------
def criar_aluno(idALUNO, nome):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o id tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  if aluno_existe(idALUNO):
    return 'O Aluno(a) já foi criado anteriormente.'
  if not aluno_menor100():
    return 'Embora este idALUNO ainda não existe, o limite de 100 alunos cadastrados já foi atingido.'

  nome = texto_upper(nome)
  # Cria aluno/a
  ALUNO[str(idALUNO)] = {'nome': nome,
                         'provas_aluno':{}}
  texto = []
  texto.append('Novo aluno(a) cadastrado(a):')
  texto.append('idALUNO: {}, nome: {}'.format(idALUNO, nome))
  return texto

#TIPO GET ALUNO ---------------------------------------------------------------------------
def info_aluno(idALUNO):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o id tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  if not aluno_existe(idALUNO):
    return 'O Aluno(a) ainda não foi criado.'

  x = ALUNO[str(idALUNO)]
  info_aluno = []
  info_aluno.append(['idALUNO: {}, Nome: {}'.format(str(idALUNO), x['nome'])])
  x_p = ALUNO[str(idALUNO)]['provas_aluno']
  for k,v in x_p.items():
    info_aluno.append('Prova:' + str(k) + ', [Questão, resposta]-->  ' + str(v[1:]))
  return info_aluno

#TIPO GET ALUNOS ---------------------------------------------------------------------------
def info_total_alunos():
  texto = []
  texto2 = []
  for k,v in ALUNO.items():
    texto.append('Aluno(a) {}, {}'.format(k, v['nome']))
  texto2.append('Alunos(as) Cadastrados(as):')
  texto2.extend(sorted(texto))
  return texto2

#TIPO POST PROVA PARA ALUNO ------------------------------------------------------------------
def criar_prova_aluno(idALUNO, idPROVA):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  if not id_valido(idPROVA):
    return 'O valor inserido para o idPROVA tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  idPROVA = id_upper(idPROVA) #Transforma o idALUNO em uppercase
  if not aluno_existe(idALUNO):
    return 'O Aluno(a) {} ainda não consta no sistema.'.format(idALUNO)
  if not prova_existe(idPROVA):
    return 'A prova {} não consta no sistema.'.format(idPROVA)
  if aluno_prova_existe(idALUNO, idPROVA):
    return 'O Aluno(a) {} já tem a prova {} em seu cadastro.'.format(idALUNO, idPROVA)
 
  ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)] = []
  texto = 'A prova {} foi cadastrada para o(a) aluno(a) {}.'.format(idPROVA, idALUNO)
  return texto

#TIPO POST QUESTAO_ALUNO_PROVA ------------------------------------------------------------
def preencher_prova_aluno(idALUNO, idPROVA, q, resposta):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  if not id_valido(idPROVA):
    return 'O valor inserido para o idPROVA tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  idPROVA = id_upper(idPROVA) #Transforma o idALUNO em uppercase
  if not aluno_existe(idALUNO):
    return 'O Aluno(a) {} ainda não consta no sistema.'.format(idALUNO)
  if not prova_existe(idPROVA):
    return 'A prova {} não consta no sistema.'.format(idPROVA)
  if not aluno_prova_existe(idALUNO, idPROVA):
    return 'O Aluno(a) {} não tem a prova {} em seu cadastro.'.format(idALUNO, idPROVA)
  if not int_positivo(q):
    return 'Ops! O valor inserido para o número da questão é menor que 1.'
  if not q_menor_totalq(idPROVA, q):
    return 'Ops! O número de questão escolhido é diferente do número de questões que a prova tem.'  
  if not func_alternativa(resposta):
    return 'Ops! O valor inserido para a resposta da pergunta não é A, B, C, D ou E.'
  else:
    alternativa = func_alternativa(resposta)

  #Se os campos de questões ainda não foi criado:
  if ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)] == []:
    criar_lists_info_quest_ALUNOS(idALUNO, idPROVA) #cria lista vazia de respostas para aluno(a)
  # Preenchimento da questão
  ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)][q] = [int(q), str(alternativa)]
  texto = []
  texto.append('idALUNO: {}'.format(idALUNO))
  texto.append('idPROVA: {}'.format(idPROVA))
  x = (ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)])
  for i in range(1,len(x)):
    texto.append('Questão: {}, Resposta: {}'.format(str(x[i][0]), str(x[i][1])))
  return texto

#TIPO GET PROVA DE ALUNO ----------------------------------------------------------------------
def info_prova_aluno(idALUNO, idPROVA):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  if not id_valido(idPROVA):
    return 'O valor inserido para o idPROVA tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  idPROVA = id_upper(idPROVA) #Transforma o idALUNO em uppercase
  if not aluno_existe(idALUNO):
    return 'O Aluno(a) {} ainda não consta no sistema.'.format(idALUNO)
  if not prova_existe(idPROVA):
    return 'A prova {} não consta no sistema.'.format(idPROVA)
  if not aluno_prova_existe(idALUNO, idPROVA):
    return 'O Aluno(a) {} não tem a prova {} em seu cadastro.'.format(idALUNO, idPROVA)
  x = ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)]
  if x == []:
    return 'Embora a prova {} esteja cadastrada para {}, não há nenhuma resposta postada ainda.'.format(idPROVA, idALUNO)

  info = []
  info.append('Aluno(a): {}'.format(idALUNO))
  info.append('Prova: {}'.format(idPROVA))
  info.append('Número total de questões: {}'.format(x[0]))
  for quest in range (1,len(x)):
    info.append('Questão: {}, Resposta: {}'.format(x[quest][0],x[quest][1]))
  return info

#TIPO GET NOTAS ALUNO -------------------------------------------------------------------------
def info_notas_aluno(idALUNO):
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  notas_provas = []
  notas_provas.append('MÉDIA PONDERADA PARA CADA PROVA')
  notas_provas.append([str(idALUNO), str(ALUNO[str(idALUNO)]['nome']) ])
  provas_computaveis = provas_computaveis_aluno (idALUNO) # Retonra uma lista com o idALUNO em [0] e idPROVA [1:] das provas com tudo pronto para computar nota para o aluno em questão
  if provas_computaveis == []:
    notas_provas.append(['Não há nenhuma prova com todas as questões já preenchidas e/ou com todas as respostas por aluno lançadas'])
  else: 
    n = len(provas_computaveis)
    for i in range(1,n):
      prova = str(provas_computaveis[i])
      nota = calcula_nota(idALUNO, prova)
      notas_provas.append([str(prova), str(PROVA[str(prova)]['título']), 'Nota = ' + str(nota)[0:3]])
  notas_provas.append(['*** Provas incompletas ou com respostas de aluno(a) incompletas não são contabilizadas'])
  return notas_provas

# TIPO GET APROVADOS -------------------------------------------------------------------------
def aprovados():
  p_completas = []
  p_completa_aluno = []
  p_completas.extend(sorted(provas_completas()))  
  if p_completas == []:
    return 'Não há nenhuma prova completa para gerar a lista de aprovados.'
  alunos_keys = []
  alunos_keys.extend(sorted(ALUNO.keys()))
  if alunos_keys == []:
    return 'Não há nenhum(a) aluno(a) para gerar a lista de aprovados.'
  # Dicionário com todos os alunos que retorna: incompleto, aprovado ou nao aprovado.
  dict_final = {}
  for idALUNO in alunos_keys:
    dict_final[str(idALUNO)] = {'nome': str(ALUNO[str(idALUNO)]['nome']),
                                'condição':'Incompleto'}
  lista_alunos_nota_final = []
  for idALUNO in alunos_keys: #para cada aluno
    for idPROVA in ALUNO[str(idALUNO)].keys(): #para cada prova do aluno
      p_completa_aluno.extend(aluno_provas_completas(idALUNO)) 
      if idPROVA in p_completas: #se a prova do aluno estiver na lista de provas completas
        if idPROVA in p_completa_aluno: # se a prova do aluno estiver completa
          lista_alunos_nota_final.append(idALUNO)

  for idALUNO in lista_alunos_nota_final:
    notas_aluno = []
    for idPROVA in ALUNO[str(idALUNO)].keys():
      notas_aluno.append(calcula_nota(idALUNO, idPROVA))
    nota = float(sum(notas_aluno)/len(notas_aluno))
    if nota >= 7.0:
      dict_final[str(idALUNO)]['condição'] = 'nota: {}, APROVADO'.format(nota)
    if nota < 7.0:
      dict_final[str(idALUNO)]['condição'] = 'nota: {}, não aprovado'.format(nota)
  return dict_final

# TIPO DELETE PROVA ALUNO ----------------------------------------------------------------------
def deletar_prova_aluno(idALUNO, idPROVA):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  if not id_valido(idPROVA):
    return 'O valor inserido para o idPROVA tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  idPROVA = id_upper(idPROVA) #Transforma o idALUNO em uppercase
  del ALUNO[str(idALUNO)]['provas_aluno'][str(idPROVA)]
  return 'Prova {} do aluno(a) {} deletada.'.format(idPROVA, idALUNO)

# TIPO DELETE ALUNO ----------------------------------------------------------------------
def deletar_aluno(idALUNO):
  #Condições para preencher a questão
  if not id_valido(idALUNO):
    return 'O valor inserido para o idALUNO tem mais ou menos que 4 caracteres. Tente novamente.'
  idALUNO = id_upper(idALUNO) #Transforma o idALUNO em uppercase
  del ALUNO[str(idALUNO)]
  return 'Aluno(a) {} deletado(a).'.format(idALUNO)

# TIPO DELETE PROVA ----------------------------------------------------------------------
def deletar_prova(idPROVA):
  if not id_valido(idPROVA):
    return 'O valor inserido para o idPROVA tem mais ou menos que 4 caracteres. Tente novamente.'
  idPROVA = id_upper(idPROVA) #Transforma o idALUNO em uppercase
  for v in ALUNO.values():
    if idPROVA in v['provas_aluno']:
      return 'Um(a) ou mais alunos(a) tem a prova {} cadastrada; Para deletar a prova, é preciso que a mesma não esteja cadastrada para nenhum aluno(a).'.format(idPROVA)
  del PROVA['idPROVA']
  return 'A prova {} foi exlcuída com sucesso.'.format(idPROVA)