# -*- coding: utf-8 -*-
"""Main runner: build the whole business study plan."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generator_build as GB
import generator_exams as GE
import generator_docs as GD

if __name__ == "__main__":
    print("Building weeks...")
    GB.build_weeks()
    print("Building semester READMEs...")
    GB.build_readmes()
    print("Building exams...")
    GE.build_exams()
    print("Building overview + curriculum docs...")
    GD.build_docs()
    print("Done.")
