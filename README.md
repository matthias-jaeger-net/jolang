# jolang
Python program to compile jolang to javascript

```
Imagine angle;
Remember radius is 300.0;

Dear computer, please: {
  Create a drawing with the format (800, 800);
  angle is 0.0;
}

Dear computer, please animate: {
  Fill the background with (0);
  Remember x is cosinus of (angle) times radius;
}

```

jolang adds syntactic sugar to your p5 sketches. It extends JavaScript and p5's langugae to make it less forgiving, more emotional, and even painful to write creative programs.

Extremly polite expressions act as intuitive replacements for common JavaScript keywords, operators, and p5's most popular methods. You can continue to use raw JavaScript inside jolang, and the `jolang` transpiler will convert your code into raw JavaScript.

### Installation

jolang requires [python3](https://www.python.org/).



# Usage:
- Clone the repository
- Replace the code in ``sketch.jolang`` with your own code.
- Change directory to the ``code`` folder
- Call: ``python3 compile.py``
- A file called ``sketch.js`` will be compiled


#### Keywords

| jolang | JavaScript |
| ----- | ----- |
| FIX OIDA | const |
| OIDA | let |
| ALSO DES IS AMOI NIX | null |
| HAWIDERE | new |
| I BIMS | this |
| HACKL AMOI WOS | function |
| SCHLEICH DI | delete |
| SICHA NET | false |
| NA NO NA NET | true |
| WOS BISTN DU FIA A WAPPLA | instanceof |
| WEM GHERSTN DU | typeof |
| JO GLEI | await |
| OWIZAHRA | async |
| AIZAL | in |

#### Control statements

| WienerScript | JavaScript |
| ----- | ----- |
| STRAWANZ MA | for |
| DAMMA WOS | do |
| GEMMA | while |
| GUSCH | continue |
| WOS WÜSTN | if |
| WOA NUA A SCHMÄH | else if |
| A SCHO WUASCHT | else |
| WOS IS MIT DIR | switch |
| I SCHAU NUR | case |
| PASST SCHO | break |
| NA GEH | default |
| DRAH DI HAM | return |
| GEH SCHEISSN | throw |
| SCHAU MA MOL | try |
| LECK OASCH | catch |
| SAMMAS ENDLICH | finally |

#### Operators

| WienerScript | JavaScript |
| ----- | ----- |
| KANNST DA VUASTÖHN | === |
| DES GEHT SI SCHO AUS | == |
| UND ÜBRIGENS | && |
| GHUPFT WIE GHATSCHT | \|\| |
| WENNST MANST | = |
| ANS AUFI | ++ |
| AUFI | + |
| ANS OWI | -- |
| OWI | - |
| HAUTS EICH ZAM | * |
| BRÖCKERL | / |
| S'RESTL | % |
| WENGA | < |
| GRESSA | > |
| HOIT NET GRESSA | <= |
| HOIT NET KLANA | >= |
| JO EH | ! |
| HOST MI | ? |
| DANN HOIT NET | : |
| HUACH ZUA | => |

#### Functions

| WienerScript | JavaScript |
| ----- | ----- |
| I MAN JA NUR | console.log |
| DO IS DA HUND BEGROBN | console.debug |
| GSCHISSN GRISSN | console.error |
| DES IS MA ECHT Z'DEPPAT | process.exit |
| HEAST | alert |

## License
This project is licensed under the MIT license, Copyright (c) 2020 David Pichsenmeister | [pichsenmeister.com](https://pichsenmeister.com). For more information see [LICENSE](LICENSE).


Made by [@pichsenmeister](https://twitter.com/pichsenmeister). Inspired by [ArnoldJS](https://github.com/theBrianCui/ArnoldJS).
