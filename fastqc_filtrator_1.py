#!/usr/bin/env python3

import sys

fasta_file = (sys.argv[1])
file_arg = sys.argv[2:]
min_length = 0  # почитать задание что там сказано
gc_counter = False
out_non_filtered = False
file_name = False  # File name flag

for i in file_arg:
    if i == "--min_length":
        i = file_arg.index("--min_length")
        min_length = files[i + 1]

    elif i == "--keep_filtered":
        out_non_filtered = True

    elif i == "--gc_bounds":
        i = file_arg.index("--gc_bounds")
        min_gc = int(file_arg[i + 1])
        gc_counter = True
        try:
            max_gc = int(file_arg[i + 2])
        except ValueError:
            max_gc = min_gc
    elif i == "--output_base_name":
        j = file_arg.index("--output_base_name")
        names = file_arg[j+1]
        file_name = True

if file_name is True:
    filtered = names + "_filtered.fasta"
    failed = names + "_failed.fasta"
else:
    names = fasta_file[:-6]
    filtered = names + "_filterd.fasta"
    failed = name + "_failed.fasta"

if out_non_filtered is True:
    filtered_file = open(filtered, "w")
    non_filtered = open(failed, "w")
else:
    filtered_file = open(good, "w")


def lenght_filtration(line1, min_length):
    min_length = int(min_length)
    init_length = int(line1.split("=")[1])
    if init_length >= min_length:
        return True
    else:
        return False


def gc_counting_f(line2, min_gc, max_gc):

    min_GS = int(min_gc)
    max_GS = int(max_gc)
    all_bases = len(line2)
    c, g = line2.count("C"), line2.count("G")
    gc_content = float((c + g) / all_bases) * 100)
    if max_GS == min_GS:
        if min_GS <= gc_content:
            return True
        else:
            return False
    else:
        if min_GS <= gc_content <= max_GS:
            return True
        else:
            return False


def output_files(line1, line2, line3, line4, lenght_filtration, gc_counting_f):
    if lenght_filtration is True and gc_counting_f is True:
        filtered.write(line1 + "\n")
        filtered.write(line2 + "\n")
        filtered.write(line3 + "\n")
        filtered.write(line4 + "\n")
    elif out_non_filtered is True:
        failed.write(line1 + "\n")
        failed.write(line2 + "\n")
        failed.write(line3 + "\n")
        failed.write(line4 + "\n")
    else:
        pass


with open(fasta_file, "r") as fs:
    line1: str = fs.readline().rstrip("\n")
    while line1 != "":
        line2, line3, line4 = fs.readline().rstrip("\n"), fs.readline().rstrip(
            "\n"), fs.readline().rstrip("\n")
        lenght_filter = lenght_filtration(line1, min_length)
        if gc_counter is True:
            gc_filter = gc_counting_f(line2, min_gc, max_gc)
        else:
            gc_filter = True
        output_files(line1, line2, line3, line4, lenght_filter, gc_filter)
        line1 = fs.readline().rstrip("\n")

    if out_non_filtered is True:
        filtered.close()
        failed.close()
    else:
        filtered.close()
