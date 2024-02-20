#Atividade 19 - Biologia estrutural

# # # DESAFIO REGENERA # # # Resolução Bryan Tavares

# Recuperação de sequência de proteases de Pseudoalteromonas phenolica

from Bio import SeqIO

# entrada = "genoma.fasta"
# saida = "sequencias_recuperadas.fasta"

fasta_file = "teste_01.fasta"

with open(fasta_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print("ID:", record.id)
        print("Descrição:", record.description)
        print("Sequência:", record.seq)
        print("---")



# # # B. A. R. T. # # # Resolução Bryan Tavares

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <
