"""Adapted from https://github.com/selimb/cookiecutter-latex-article

This file is Under MIT license.
"""

import os
import shutil
import json

def check_true(option):
    """Check if option is true.

    Account for user inputting.
    """
    option = option.lower()
    if option == 'yes':
        return True
    else:
        return False

def process_bibtex(bibtex, tex_root):
    """Act on ``bibtex`` option.

    Parameters
    ----------
    bibtex : bool
        If True, nothing is done.
        Else, delete dabib.bib
    tex_root : str
        Path to root of LaTeX project.
    """
    if not bibtex:
        bibtex_path = os.path.join(tex_root, 'bibliography.bib')
        os.remove(bibtex_path)

def process_add_examples(add_examples, tex_root):
    """Act on ``add_examples`` option.

    Parameters
    ----------
    add_examples : bool
        If True, nothing is done.
        Else, delete ./figs/bear.jpg
    tex_root : str
        Path to root of LaTeX project.
    """
    if not add_examples:
        figs_path = os.path.join(tex_root, 'figs')
        os.remove(os.path.join(figs_path, 'bear.jpg'))


if __name__ == '__main__':
    root_path = os.path.join(os.getcwd())
    with open('options.json','r') as f:
        options = json.load(f)
        process_bibtex(check_true(options['bibtex']), root_path)
        process_add_examples(check_true(options['add_examples']), root_path)
    os.remove(os.path.join(root_path, 'options.json'))
    os.remove(os.path.join(root_path, 'license.tex'))
