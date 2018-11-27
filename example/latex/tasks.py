from invoke.collection import Collection

from hocus_pocus.tex import compile_latex


ns = Collection(compile_latex)
ns.configure({"compile_latex": {"texfile": "mwe.tex"}})
