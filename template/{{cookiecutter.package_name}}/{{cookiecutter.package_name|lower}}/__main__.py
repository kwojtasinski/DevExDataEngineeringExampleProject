from {{cookiecutter.package_name|lower}}.cli import parser
from {{cookiecutter.package_name|lower}}.module import add

args = parser.parse_args()

print(add(*args.n))
