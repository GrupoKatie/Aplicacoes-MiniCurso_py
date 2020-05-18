nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno Aprovado")

if media >= 5 and media < 7:
    print("Ficou de Recuperação")

if media < 5:
    print("Aluno Reprovado")
