# thaibraille
Thai Braille for Natural Language Processing.

**Note**: As of the latest version, Thaibraille uses the **international standard Braille dot numbering system** (ISO/ANSI) for better compatibility with the global Braille community. This ensures that internal representations align with standards used in EU, UK, US, and the Unicode Braille Patterns specification.

สวัสดีชาวโลก
> ⠎⠺⠖⠎⠓⠌ ⠦⠡⠺⠊⠍⠛

## Install

> pip install thaibraille

## Usage

**Thai word to braille**

```python
from thaibraille import thai_word_braille

print(thai_word_braille("แมว"))

# output: ⠩⠇⠺
```

This function support Thai and number only.

**Thai text to braille**

```python
from thaibraille import thai_text_braille

print(thai_text_braille("แมวกิน ปลา"))

# output: ['⠩⠇⠺', '⠛⠉⠗', ' ', '⠯⠍⠡']
```

This function support Thai and number only.

## License


```
   Copyright 2023 Wannaphong Phatthiyaphaibun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 ```
