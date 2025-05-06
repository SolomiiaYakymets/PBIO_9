import random

nucleotides = ['A', 'C', 'G', 'T']


def write_fasta(seq_id, seq_description, sequence):
    with open(seq_id + ".fasta", 'w') as f:
        f.write(f">{seq_id} {seq_description}\n")
        for i in range(0, len(sequence), 80):
            f.write(sequence[i:i+80] + '\n')


def calculate_statistics(sequence):
    length = len(sequence)
    counts = {nuc: sequence.count(nuc) for nuc in 'ACGT'}

    print("\nSequence Statistics:")
    for nuc in 'ACGT':
        percentage = (counts[nuc] / length) * 100
        print(f"{nuc}: {percentage:.2f}%")

    gc = counts['G'] + counts['C']
    at = counts['A'] + counts['T']

    if at == 0:
        print("Undefined")
    else:
        ratio = gc / at
        print(f"CG%AT: {ratio:.2f}")


sequence_length = int(input("Enter the sequence length: "))
sequence_id = input("Enter the sequence id: ")
sequence_description = input("Enter the sequence description: ")
user_name = input("Enter your name: ")

dna_sequence = []
for i in range(sequence_length):
    dna_sequence.append(random.choice(nucleotides))

dna_sequence = "".join(dna_sequence)

random_pos = random.randint(0, sequence_length)
dna_sequence_with_name = dna_sequence[:random_pos] + user_name + dna_sequence[random_pos:]

write_fasta(sequence_id, sequence_description, dna_sequence_with_name)
calculate_statistics(dna_sequence)
