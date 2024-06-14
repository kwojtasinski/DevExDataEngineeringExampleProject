import argparse

parser = argparse.ArgumentParser(prog="{{cookiecutter.package_name}}")

parser.add_argument("n", nargs="+", type=int)
