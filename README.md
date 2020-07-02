# jolang

**jolang** adds syntactic sugar to your p5 sketches. It extends JavaScript and p5's langugae to make it less forgiving, more emotional, and even painful to write creative programs. Extremly polite expressions act as intuitive replacements for common JavaScript keywords, operators, and p5's most popular methods. You can continue to use raw JavaScript inside jolang, and the `jolang` transpiler will convert your code into raw JavaScript.

## jolang
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
  Remember y is sinus of (angle) times radius;
}
```
## JavaScript
```javascript
// transpiled from jolang
let angle;
const radius = 300.0;

function setup () {
  createCanavs (800, 800);
  angle = 0.0;
}

function draw () {
  background (0);
  const x = cos(angle) * radius;
  const y = sin(angle) * radius;
}

```



## Installation

jolang requires [python3](https://www.python.org/).



## Usage:
- Clone the repository
- Replace the code in ``sketch.jolang`` with your own code.
- Change directory to the ``code`` folder
- Call: ``python3 compile.py``
- A file called ``sketch.js`` will be compiled

## Javascript

#### Keywords

| JavaScript | jolang |
| ----- | ----- |
| const | Remember |
| let | Imagine |


#### Control statements

| jolang | JavaScript |
| ----- | ----- |
| STRAWANZ MA | for |

#### Operators

| WienerScript | JavaScript |
| ----- | ----- |
| equals exactly | === |
| equals | == |
| is | = |

#### Functions

| WienerScript | JavaScript |
| ----- | ----- |
| I MAN JA NUR | console.log |
| DO IS DA HUND BEGROBN | console.debug |
| GSCHISSN GRISSN | console.error |
| DES IS MA ECHT Z'DEPPAT | process.exit |
| HEAST | alert |

## License
This project is licensed under the MIT license, Copyright (c) 2020 Matthias Jäger.

Inspired by [@pichsenmeister](https://twitter.com/pichsenmeister) and [ArnoldJS](https://github.com/theBrianCui/ArnoldJS).
