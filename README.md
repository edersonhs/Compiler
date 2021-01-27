# Lexical Analyser
Lexical analyzer developed in the discipline of Compilers during the Computer Science Course at Unifacvest. 

### Example Code
```
1  - print("Ignored Content");
2  - 
3  - @var = 10 //One line comment
4  - 
5  - 34var = 10
6  - 
7  - print(50 == 5)
8  - 
9  - /*
10 - Comment block
11 - to be ignored
12 - */
13 - 
14 - test *= 'Ignored Content';
```

 ### Output Preview:
![preview](https://github.com/edersonhs/Lexical_Analyser/blob/master/images/Output-Preview.png?raw=true)


## Example Language
| **Rules**                                                    | **Example**                             |
|--------------------------------------------------------------|-----------------------------------------|
| Identifier cannot start with number                          | 2identifier, 13number, 34var            |
| Only characters defined in the language alphabet are allowed | (A...Z), (a...z) (0...9), operators, delimiters |

| **Key_Worlds** | **Operators** | **Delimiters** |
|----------------|---------------|----------------|
|       int      |       +       |        ;       |
|      float     |       -       |        {       |
|     string     |       *       |        }       |
|     boolean    |       /       |        (       |
|      char      |       %       |        )       |
|      void      |       =       |        [       |
|     double     |       >       |        ]       |
|     public     |       <       |       //       |
|     private    |       >=      |       /*       |
|      igor      |       <=      |       */       |
|      vasco     |       !       |        "       |
|     return     |       !=      |        '       |
|       if       |       ==      |        ,       |
|      else      |       &       |                |
|       for      |       \|      |                |
|      while     |       ++      |                |
|      break     |       --      |                |
|    continue    |       +=      |                |
|     funcao     |       -=      |                |
|      hame      |               |                |
|      true      |               |                |
|      false     |               |                |
|     switch     |               |                |
|      case      |               |                |
|     default    |               |                |
|      print     |               |                |
