"""
Inteiros todos os números inteiros

Real todos os números reais, utilizando o separador . (ponto) para separa o inteiro do fracionário

Operadores + - * / % = > < >= <= ! != == & | ++ -- += -= /= *=

Delimitadores ; { } ( ) [ ] // /* */ “ ‘

Palavras reservadas int float string boolean char void double public private igor vasco return if else for while break
continue funcao hame true false switch case default

Identificador qualquer outra palavra respeitando o alfabeto da linguagem este é [A...Z][a...z][0...9][ _ ]

Qualquer carácter que não presente em nosso alfabeto deverá gerar um erro léxico (eliminando operadores e delimitadores
que entrariam como palavras de nossa linguagem)

OBSERVAÇÃO: adicionei o _ como um carácter válido e os operadores ++(incremento unitário, -- (decremento unitário), +=,
-= , /= e *=, nossa linguagem é case sensitive
"""
from menu import *

menu('Analisador Léxico', 'Sair do Sistema')
