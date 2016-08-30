#!/usr/bin/env python

import os
import subprocess as sp
import sys
import shutil

PSMC_PLOT_PATH  = "/psmc/utils/psmc_plot.pl"
GENERATION_TIME = "3.5"
MUTATION_RATE   = "4.4e-10"

def get_paths():
    for path in sys.argv[1:]:
        yield os.path.abspath(path)

def walk_item(path):
    for cur, sub, files in os.walk(path):
        for fi in files:
            full_path = os.path.join(cur, fi)

            if full_path.endswith(".psmc"):
                is_psmc = True
            else:
                is_psmc = False

            base_name = os.path.basename(fi).rsplit('.',2)[0]
            yield full_path, base_name, is_psmc


def run_non_bootstrapped_plot(path, base_name):
    cmd = [PSMC_PLOT_PATH,
           '-RM', base_name.rsplit("_",1)[-1],
           '-u', MUTATION_RATE,
           '-g', GENERATION_TIME,
           base_name,
           path]
    sp.call(cmd)


def run_bootstrapped_plot(path, base_name):
    cmd = [PSMC_PLOT_PATH,
           '-R',
           '-u', MUTATION_RATE,
           '-g', GENERATION_TIME,
           base_name,
           path]
    sp.call(cmd)


def make_text_dir():
    files = os.listdir(os.getcwd())

    if not os.path.isdir("txtfiles"):
        os.makedirs("txtfiles")
    else:
        sp.call(['rm', '-r', 'txtfiles'])
        os.makedirs('txtfiles')

    for fi in files:
        if fi.endswith(".gp") or \
        fi.endswith(".eps") or \
        fi.endswith(".par"):
            os.remove(fi)
        elif fi.endswith("txt"):
            if not fi == "simus_plot.txt":
                shutil.move(fi, "txtfiles")
    shutil.copy("simus_plot.txt", 'txtfiles')
    os.chdir("txtfiles")
    sp.call(['gnuplot', 'simus_plot.txt'])


def main():
    for abs_path in get_paths():
        for path, base_name, is_psmc in walk_item(abs_path):
            if base_name.startswith("mass"):
                if is_psmc:
                    run_non_bootstrapped_plot(path, base_name)
            elif base_name.startswith("round"):
                run_bootstrapped_plot(path, base_name)
    make_text_dir()


if __name__ == "__main__":
    main()
