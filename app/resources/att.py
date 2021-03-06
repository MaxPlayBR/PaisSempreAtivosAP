from requests import get
import json,base64,re

def getFaltas(matricula,password):
    freq = "http://aluno.seduc.ce.gov.br/api/dados_service/frequencia"
    faltas = 0
    
    base = str(matricula)+":"+str(password)
    en = base64.b64encode(base.encode('ascii'))
    b64user = en.decode('ascii')

    headers={
        'Authorization':'Basic '+b64user,
        'User-Agent':'okhttp/3.3.0',
        'Accept-Encoding':'gzip',
        'Host':'aluno.seduc.ce.gov.br',
        'AppVersionName':'1.2',
        'AppVersionName':'4',
        'Accept':'application/json',
        'Cache-Control':'no-cache'
    }
    
    r = get(freq,headers=headers).text
    rj = json.loads(r)    
    fq = re.findall(r"(?!\:)\d(?=\,)",str(rj))
    
    for nt in fq:
        faltas+=int(nt)
        
    return faltas
    
def getMedias(matricula,password):
    bl="http://aluno.seduc.ce.gov.br/api/dados_service/boletim"
    
    materias = []
    
    base = str(matricula)+":"+str(password)
    en = base64.b64encode(base.encode('ascii'))
    b64user = en.decode('ascii')

    headers={
        'Authorization':'Basic '+b64user,
        'User-Agent':'okhttp/3.3.0',
        'Accept-Encoding':'gzip',
        'Host':'aluno.seduc.ce.gov.br',
        'AppVersionName':'1.2',
        'AppVersionName':'4',
        'Accept':'application/json',
        'Cache-Control':'no-cache'
    }
    
    r = get(bl,headers=headers).text
    rj = json.loads(r)
    
    fd = re.findall(r"(?!\:)[0-9.]+(?=\, \'n)",str(rj))
    
    for i in fd:
        if float(i)<=6:
            materias.append(i)
    
    return materias