# Escola_ALF_API

# API PARA CADASTRO DE NOTAS E ALUNOS DA ESCOLA ALF

## Descrição:
O aplicativo permite o cadastro de:
 --> Provas com perguntas, respostas e pesos e 
 --> Alunos com provas realizadas e suas respectivas respostas.

 É possível também:
--> Gerar o boletim do(a) aluno(a) para cada prova,
--> Gerar o boletim de alunos aprovados/não aprovados pela média arimtética geral de todas as provas. 


## Rodar localmente

1. Instalar, caso ainda não tenha instalado:
```
pip install fastapi
pip install uvicorn[standard]
```

2. Rodar o servidor local:
---> Vá até a pasta 'Codigo_Escola_ALF' baixada em seu computador e na parte superior da pasta, onde se encontra o endereço da pasta,
digite 'CMD' que te direcionará ao prompt. Basta colar o texto 'uvicorn main:app --reload' no prompt e apertar enter. 
```
uvicorn main:app --reload
```

3. Na URL, digite o código abaixo para rodar a API:
```
http://127.0.0.1:8000/docs#/
```
Ou, caso prefira:
```
http://localhost:8000/
```


## Bibliotecas e arquivos utilizados
 - FastAPI
 - Escola_ALF_Codigo_Logica.py
 - main.py


## Organização do sistema
### PROVA
 - Para cadastrar uma prova é preciso informar um código de 4 caracteres que será o idPROVA, o número de perguntas da prova e o título da prova, 
 - Só é possível deletar uma prova caso nenhum aluno tenha a mesma cadastrada. Neste caso, basta deletar o cadastra da devida prova para todos os alunos que têm a mesma em seu cadastro,
 - As respostas e pesos de cada pergunta de uma prova só podem ser geradas depois de gerar a prova em si,
 - O cadastro de pesos e respostas de uma prova é feito pergunta por pergunta e sempre pode ser modificado.
 - É possível deletar todas as respostas de uma prova para preenche-la novamente,
 - Todo conteúdo referente ao idPROVA é armazenado e um dicionário chamado'PROVA'.

### ALUNO
- Para cadastrar um aluno(a) é preciso informar um código de 4 caracteres que será o idALUNO, e nome do aluno(a),
- O sitema permite o cadastro máximo de 100 alunos,
- Só é possível cadastrar uma prova para um aluno(a) depois que tanto o aluno(a) quanto a prova já existem,
- Só é possível cadastrar as respostas de uma prova realizada pelo aluno(a) depois que a prova já foi cadastrada para o estudante,
- O cadastro de respostas realizadas pelo aluno(a) é feito pergunta por pergunta e sempre pode ser modificado,
- Sempre é possível deletar um aluno(a),
- Sempre é possível deletar uma prova do cadastro de um aluno(a),
- Todo conteúdo referentes ao idALUNO (inclusive as provas realizadas pelo aluno) é armazenado em um dicionário chamado 'ALUNO'. 


### BOLETIM
- É possível gerar o boletim de cada aluno informando o idALUNO,
- As notas do aluno não são armazenadas no sistema para que mudanças de peso e respostas de questões não ocasionem resultados diferentes. Portanto, toda vez que o boletim for requisitado, um novo cálculo de notas é feito. 
--> O boletim só apresenta as provas que têm todas as questões cadastradas (com resposta e peso de questão) e com todas as respostas do aluno já inseridas em seu idALUNO.

### APROVADOS
- O dicionário de aprovados utiliza a média aritmética de todas as provas. Alunos(as) com nota igual ou superior à 7.0 são 'aprovado', notas inferiores são classificadas como 'não aprovado'.
- Quando uma prova está incompleta, seja as respostas do(a) aluno(a) ou as respostas e os pesos da própria prova, o idALUNO é classificado como 'incompleto' a nota de 7.0 para designar os aprovados. Notas inferiores classificam o aluno em não aprovado.


## Funções disponíveis:
### "get/{idPROVA}" 
- API GET que retorna informações de uma prova cadastrada;
É preciso informar:
 -- idPROVA (str): 4 caracteres com o idPROVA.


### "get/PROVAS"
- API GET que retorna todas as provas cadastradas;
Não é preciso informar nenhum parâmetro. 


### "post/{idPROVA}" 
- API POST que posta uma prova no cadastro;
É preciso informar:
-- idPROVA (str): 4 caracteres com o idPROVA,
-- titulo (str): texto que remete ao título da prova,
-- n_questões (int): total de questões que a prova tem.


### "post/idPROVA/{questao}" 
- API POST que posta uma pergunta para uma prova já cadastrada;
É preciso informar:
-- idPROVA (str): 4 caracteres com o idPROVA,
-- q (int): número da questão, que precisa estar entre 0 e o total de questões que a prova tem,
-- resposta (str): alternativa 'A', 'B', 'C', 'D' ou 'E',
-- peso (int): valor inteiro maior que 1. 


### "get/{idALUNO}"
- API GET que retonra informações sobre um aluno;
É preciso informar:
-- idPROVA (str): 4 caracteres com o idPROVA.


### "get/ALUNOS"
- API GET que retonra informações sobre todos os alunos;
Não é preciso informar nenhum parâmetro. 


### "post/{idALUNO}" 
- API POST que gera um aluno(a);
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO,
-- nome (str): texto com o nome do aluno(a).


### "get/idALUNO/{idPROVA}" 
- API GET que retonra as informações de uma prova específica cadastrada para um aluno(a);
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO,
-- idPROVA (str): 4 caracteres com o idPROVA.


### "post/idALUNO/{idPROVA}" 
- API POST que cadastra uma prova para um aluno(a) já existente;
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO,
-- idPROVA (str): 4 caracteres com o idPROVA.


### "post/idALUNO/idPROVA/{questao}" 
- API POST que cadastra uma resposta para uma prova já cadastrada em um idALUNO;
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO,
-- idPROVA (str): 4 caracteres com o idPROVA,
-- q (int): número da questão, que precisa estar entre 0 e o total de questões que a prova tem,
-- resposta (str): alternativa 'A', 'B', 'C', 'D' ou 'E'.


### "get/BOLETIM/{idALUNO}"
- API GET que gera o boletim para cada aluno;
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO.


### "get/get_APROVADOS"
- API GET que gera o dicionário de aprovados/não aprovados/incompletos;
Não é preciso informar nenhum parâmetro. 


### "delete/{idPROVA}"
- API DELETE que deleta um idPROVA caso nenhum aluno tenha a prova cadastrada para si;
É preciso informar:
-- idPROVA (str): 4 caracteres com o idPROVA.

### "delete/{idALUNO}"
- API DELETE que deleta um idALUNO e suas informações;
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO.


### "delete/idALUNO/{idPROVA}"
- API DELETE que deleta uma idPROVA de um idALUNO;
É preciso informar:
-- idALUNO (str): 4 caracteres com o idALUNO,
-- idPROVA (str): 4 caracteres com o idPROVA.


## EXEMPLO DA ESTRUTURA DOS DADOS:
### ALUNO
ALUNO = {'AL10':{'nome':'ANDRÉ VEIGAS LEÃO',
                 'provas_aluno':{'IN00':[2, [1, 'C'], [2, 'D']],
                                 'L022':[3, [1, 'B'], [2, 'D'], [3, 'E']],
                                 'FI00':[]}},
         'NL15':{'nome':'NILA LOPES',
                 'provas_aluno':{'IN00':[2, [1, 'C'], [2, 'D']],
                                 'L022':[3, [1, 'B'], [2, 'D'], [3, 'E']]}},
         'LF16':{'nome':'LEILA FAGUNDES DA SILVA',
                 'provas_aluno':{'IN00':[],
                                 'L022':[3, [1, 'B'], [2, 'D'], [3, 'E']]}},      
} 


### PROVA
PROVA = {'LO00':{'título': 'PROVA DE LOGÍSTICA',
                   'n_questões': 3,
                   'info_questões':[['Questão', 'Resposta', 'Peso'], [1, 'B', 1], [2, 'D', 1], [3, 'A', 1]]},
           
           'IN00':{'título': 'PROVA DE INGLÊS',
                   'n_questões': 2,
                   'info_questões':[['Questão', 'Resposta', 'Peso'], [1, 'C', 2], [2, 'A', 3]]},

           'FR02':{'título': 'PROVA DE FRANCÊS - NIVEL 2',
                   'n_questões': 4,
                   'info_questões':[]},  
         
           'FI05':{'título': 'PROVA DE FÍSICA - 05',
                   'n_questões': 2,
                   'info_questões':[['Questão', 'Resposta', 'Peso'], [1, 'A', 1], [2, 'A', 1]]},

           'MATE':{'título': 'PROVA DE MATEMÁTICA GERAL',
                   'n_questões': 2,
                   'info_questões':[['Questão', 'Resposta', 'Peso'], [1, 'A', 1], [2, 'A', 1]]},      
}
