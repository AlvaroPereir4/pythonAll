def calcular_media(notas_aluno):
    if not notas_aluno: 
        return "0.00"

    soma_notas = sum(notas_aluno)
    media = soma_notas / len(notas_aluno)
    return f"{media:.2f}"  

if __name__ == "__main__":
    num_alunos = int(input())
    dados_dos_alunos = {}

    for _ in range(num_alunos):
        nome, *notas = input().split() 
        notas = [float(nota) for nota in notas] 
        dados_dos_alunos[nome] = notas

    nome_consulta = input()
    notas_aluno = dados_dos_alunos.get(nome_consulta, [])  

    media = calcular_media(notas_aluno)
    print(media)
